import requests
from client.config import BASE_URL

def ping_server():
    # ✅ Matches your FastAPI endpoint exactly
    url = f"{BASE_URL}/ping"
    payload = {"data": "ping"}
    response = requests.post(url, json=payload)
    response.raise_for_status()  # will raise an error if server returns 4xx/5xx
    return response.json()
