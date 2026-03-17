import requests
import os

DATAFINITI_TOKEN = os.getenv("DATAFINITI_TOKEN")

def get_properties():

    url = "https://api.datafiniti.co/v4/properties/search"

    headers = {
        "Authorization": f"Bearer {DATAFINITI_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "query": "country:US AND type:house",
        "num_records": 10
    }

    r = requests.post(url, headers=headers, json=payload)

    if r.status_code == 200:
        return r.json().get("records", [])

    return []
