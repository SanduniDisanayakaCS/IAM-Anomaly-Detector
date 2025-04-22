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

🔗 [Click here to try the live version](https://sandunidisanayakacs-iam-anomaly-detector.streamlit.app)  
*(Replace with your actual Streamlit URL)*

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
source .venv/bin/activate  # or .venv\Scripts\Activate on Windows
pip install -r requirements.txt

▶ Run the app
streamlit run app/main.py


📄 How to Use With Other Datasets
You can upload any IAM-like dataset in .csv format — it must include at least the following:

Column Name | Description
eventTime | ISO format timestamp
userIdentity | Username or user ID
eventName | IAM event name (ListBuckets, etc)
sourceIPAddress | IP address of requester
awsRegion | Region (us-east-1, etc)
userAgent | Access tool (aws-cli, browser)
responseElements | Status (Success, Failed)

✅ Column names must match. No changes are needed in the code if these columns exist.


🔍 How It Works (Behind the Scenes)
Upload your CSV

App:

Parses time, encodes all categorical features

Trains Isolation Forest in real-time

Predicts anomaly column: 1 = normal, -1 = anomaly

Visual output using matplotlib + seaborn

🌐 Deploy It Yourself (Streamlit Cloud)
Push your repo to GitHub

Go to https://streamlit.io/cloud

Select repo → main branch → set file path to:

app/main.py

📧 Contact
Author: Sanduni Disanayaka
📧 sandunidisanayaka96@gmail.com
🌍 GitHub: @SanduniDisanayakaCS


---

