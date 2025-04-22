# 🔐 IAM Anomaly Detector (Streamlit + ML)

A lightweight AI-powered app that detects **anomalous IAM (Identity and Access Management) log activity** using **Isolation Forest**, with an intuitive **Streamlit interface**. Perfect for identifying suspicious access patterns in cloud environments.

![Streamlit Badge](https://img.shields.io/badge/Live%20Demo-Streamlit-green?logo=streamlit)

---

## 📌 Features

- ✅ Upload any IAM logs in CSV format
- ✅ Auto feature extraction (time, user, event, IP, etc.)
- ✅ Real-time anomaly detection using Isolation Forest
- ✅ Interactive plots for visual analysis
- ✅ Fully deployable on Streamlit Cloud or Hugging Face Spaces

---

## 🚀 Live App

🔗 [Click here to try the live version](https://iam-anomaly-detector-version-1.streamlit.app)

---

## 📂 Folder Structure

access-anomaly-detector/ ├── app/ # Streamlit UI app │ └── main.py ├── data/ # Sample IAM logs (JSON, CSV) ├── notebooks/ # Jupyter notebook for EDA + ML │ └── eda.ipynb ├── requirements.txt # Python dependencies └── README.md # This file


---

## ⚙️ How to Run Locally

### 🔁 Clone this repo

```bash
git clone https://github.com/SanduniDisanayakaCS/IAM-Anomaly-Detector.git
cd IAM-Anomaly-Detector

🛠 Set up environment
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\Activate
pip install -r requirements.txt

▶ Run the app

streamlit run app/main.py


📄 How to Use With Other Datasets
You can upload any IAM-like dataset in .csv format — it must include at least the following columns:

Column Name | Description
eventTime | ISO format timestamp
userIdentity | Username or user ID
eventName | IAM event name (e.g., ListBuckets)
sourceIPAddress | IP address of requester
awsRegion | Region (e.g., us-east-1)
userAgent | Access tool (e.g., aws-cli)
responseElements | Status (Success, Failed)

✅ Column names must match. No changes are needed in the code if these exist.


🔍 How It Works (Behind the Scenes)
Upload your CSV file

The app:

Parses time and extracts time-based features

Encodes all categorical fields

Trains an Isolation Forest model in real-time

Predicts anomalies (1 = normal, -1 = anomaly)

Displays interactive visualizations (Matplotlib + Seaborn)

🌐 Deploy It Yourself (Streamlit Cloud)
Push your repo to GitHub

Go to https://streamlit.io/cloud

Select your repo → choose main branch → set file path to:

app/main.py


📧 Contact
Author: Sanduni Disanayaka
📧 Email: sandunidisanayaka96@gmail.com
🌍 GitHub: @SanduniDisanayakaCS

