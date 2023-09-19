import requests
import json

url = "http://127.0.0.1:8000/model_prediction"

input_data = {
    "lead_time": 0.23,
    "country": 0.16,
    "market_segment": 0.25,
    "previous_cancellations": 1.0,
    "deposit_type": 1.0,
    "booking_season": 0.5,
    "pca_column": 0.17,
    "lda_column": 0.0,
    "labels": 0.2
}

response = requests.post(url, json=input_data)

print(response.text)
