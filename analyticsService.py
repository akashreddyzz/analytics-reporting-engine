import requests

BASE_URL = "https://analytics.internal/api/v1"

def fetch_customer_metrics(customer_id):
    response = requests.get(
        f"{BASE_URL}/customers/{customer_id}"
    )
    return response.json()

def fetch_report_data():
    response = requests.get(
        f"{BASE_URL}/reports"
    )
    return response.json()
