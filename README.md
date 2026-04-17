# ✈️ Flight Data Pipeline (End-to-End AWS Project)

## 📌 Project Overview

This project is a complete end-to-end data pipeline that extracts real-time flight data from the Aviationstack API, processes it, and analyzes it using AWS cloud services.

It demonstrates a real-world data engineering workflow:

* Data Extraction (API)
* Data Ingestion (AWS Lambda)
* Data Storage (Amazon S3)
* Data Transformation (AWS Glue)
* Data Querying (Amazon Athena)

---

## 🏗️ Architecture

Pipeline Flow:

API → Lambda → S3 (Raw) → Glue → S3 (Clean) → Athena

---

## ⚙️ Technologies Used

### 🔹 Programming

* Python
* Pandas
* Requests

### 🔹 AWS Services

* AWS Lambda
* Amazon S3
* AWS Glue (ETL & Data Catalog)
* Amazon Athena
* Amazon EventBridge (Scheduling)
* Amazon CloudWatch (Monitoring)

---

## 🚀 How It Works

### 1. Data Extraction (API)

Flight data is fetched from the Aviationstack API using Python.

### 2. AWS Lambda (Automation)

Lambda function runs the script and:

* Calls the API
* Processes the response
* Uploads raw data to S3

### 3. Amazon S3 (Storage)

Data is stored in two layers:

* **Raw Layer** → Original JSON data
* **Clean Layer** → Processed CSV data

### 4. AWS Glue (ETL & Catalog)

* Crawlers detect schema
* Tables are created in Glue Data Catalog
* Data is prepared for querying

### 5. Amazon Athena (Querying)

* SQL queries are run directly on S3 data
* Enables analytics without a database

### 6. EventBridge (Scheduling)

* Automates pipeline execution (e.g., hourly/daily)

### 7. CloudWatch (Monitoring)

* Logs Lambda execution
* Helps debug pipeline issues

---

## 📂 Project Structure

```id="0g70cl"
project-folder/
│
├── script.py
├── lambda_function.py
├── .env                # Local only (ignored)
├── .gitignore
└── README.md
```

---

## 🔐 Environment Variables

Sensitive data (like API keys) are stored securely:

* Locally → `.env`
* In AWS → Lambda Environment Variables

Example:

```id="9yvd41"
API_KEY=your_api_key_here
```

---

## ▶️ How to Run Locally

1. Install dependencies:

```id="j3s0n9"
pip install requests pandas python-dotenv
```

2. Add API key in `.env`

3. Run:

```id="x3s1p5"
python script.py
```

---

## ☁️ AWS Deployment Summary

* Lambda function triggers API calls
* Data stored in S3 (raw + processed)
* Glue crawler creates tables
* Athena queries data
* EventBridge schedules execution

---

## 📊 Sample Output Columns

* flight
* airline
* from
* to
* departure_time
* arrival_time
* status
* delay

---

## 🎯 Key Learnings

* Building serverless data pipelines
* Working with real-time APIs
* Data transformation using Pandas & Glue
* Querying data using Athena
* Automating workflows with EventBridge

---

## 👨‍💻 Author

M.ISHAQ

---

## 📄 License

This project is for educational purposes.
