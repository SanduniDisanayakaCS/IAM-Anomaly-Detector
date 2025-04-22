import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import numpy as np

st.set_page_config(page_title="IAM Anomaly Detector", layout="wide")

st.title("🔐 IAM Log Anomaly Detection")
st.markdown("Upload your IAM logs in CSV format to detect suspicious access patterns.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.write(df.head())

    # Time features
    if 'eventTime' in df.columns:
        df['eventTime'] = pd.to_datetime(df['eventTime'])
        df['hour'] = df['eventTime'].dt.hour
        df['minute'] = df['eventTime'].dt.minute
        df['timestamp'] = df['eventTime'].astype(np.int64) // 10**9

    # Encode categorical
    cat_cols = ['userIdentity', 'eventName', 'sourceIPAddress', 'awsRegion', 'userAgent', 'responseElements']
    for col in cat_cols:
        if col in df.columns:
            le = LabelEncoder()
            df[col + '_encoded'] = le.fit_transform(df[col].astype(str))

    # Drop unused columns
    drop_cols = ['eventTime', 'requestParameters'] + [col for col in cat_cols if col in df.columns]
    df_engineered = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

    # Train model and predict
    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(df_engineered)
    df_engineered['anomaly'] = model.predict(df_engineered)

    st.subheader("Detected Anomalies")
    st.write(df_engineered[['anomaly']].value_counts())

    st.subheader("📊 Anomaly Visualization")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=df_engineered, x='timestamp', y='userIdentity_encoded', hue='anomaly', palette='coolwarm', ax=ax)
    st.pyplot(fig)
