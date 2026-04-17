import json
import boto3
import pandas as pd
import requests
import os
from datetime import datetime

s3 = boto3.client('s3')

# ✅ Environment variables (NO hardcoding)
BUCKET = os.environ["S3_BUCKET_NAME"]
API_KEY = os.environ["AVIATIONSTACK_API_KEY"]

URL = "http://api.aviationstack.com/v1/flights"


def fetch_api_data():
    params = {
        "access_key": API_KEY,
        "airline_iata": "PK",
        "limit": 50
    }
    response = requests.get(URL, params=params)
    return response.json()


def transform_data(data):
    df = pd.json_normalize(data['data'])

    df = df[[
        'flight.iata',
        'airline.name',
        'departure.iata',
        'arrival.iata',
        'departure.scheduled',
        'arrival.scheduled',
        'flight_status',
        'arrival.delay'
    ]]

    df.columns = [
        "flight",
        "airline",
        "from",
        "to",
        "departure_time",
        "arrival_time",
        "status",
        "delay"
    ]

    return df


def save_raw_to_s3(data):
    date = datetime.utcnow()
    path = f"flights/raw/year={date.year}/month={date.month}/day={date.day}/flights_raw.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=path,
        Body=json.dumps(data)
    )


def save_clean_to_s3(df):
    date = datetime.utcnow()
    path = f"flights/clean/year={date.year}/month={date.month}/day={date.day}/flights_clean.csv"

    csv_buffer = df.to_csv(index=False)

    s3.put_object(
        Bucket=BUCKET,
        Key=path,
        Body=csv_buffer
    )


def lambda_handler(event, context):
    raw_data = fetch_api_data()
    clean_df = transform_data(raw_data)

    save_raw_to_s3(raw_data)
    save_clean_to_s3(clean_df)

    return {
        "statusCode": 200,
        "body": "Data processed and uploaded to S3"
    }