# ✈️ Flight Data Pipeline (Aviationstack API)

## 📌 Project Overview

This project extracts real-time flight data from the Aviationstack API, processes it using Python, and saves both raw and cleaned datasets for further analysis.

It demonstrates a simple data pipeline workflow:

* Data Extraction (API)
* Data Storage (JSON)
* Data Transformation (Pandas)
* Data Export (CSV)

---

## ⚙️ Technologies Used

* Python
* Requests (API calls)
* Pandas (data processing)
* JSON
* Dotenv (environment variable management)

---

## 🚀 How It Works

### 1. Fetch Data

The script connects to the Aviationstack API and retrieves flight data for a specific airline.

### 2. Store Raw Data

The API response is saved as a raw JSON file:

* `flights_raw.json`

### 3. Transform Data

The JSON data is converted into a structured Pandas DataFrame and cleaned by selecting relevant columns.

### 4. Export Clean Data

The processed dataset is saved as:

* `flights_data.csv`

---

## 📂 Project Structure

```
project-folder/
│
├── Code.ipynb
├── .env                # API key (not pushed to GitHub)
├── .gitignore
├── flights_raw.json    # outputfile
└── flights_data.csv    # outputfile
```

---

## 🔐 Environment Variables

This project uses a `.env` file to store sensitive information.
Example:
```
API_KEY=your_api_key_here
```
Make sure `.env` is included in `.gitignore` to keep your API key secure.

---
## ▶️ How to Run

1. Install dependencies:
```
pip install requests pandas python-dotenv
```
2. Add your API key in `.env`

3. Run the script:
```
Code.ipynb
```
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
## 🎯 Future Improvements

* Automate pipeline using AWS Lambda
* Store data in Amazon S3
* Query data using AWS Athena
* Add scheduling with EventBridge
* Implement data quality checks
---
## 👨‍💻 Author
M.ISHAQ
---
## 📄 License

This project is for educational purposes.

