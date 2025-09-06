# client/main.py
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

SERVER_URL = "http://127.0.0.1:8000"   # server base URL

@app.on_event("startup")
def check_server_status():
    """Check if server is running when client starts"""
    try:
        r = requests.get(f"{SERVER_URL}/")
        if r.status_code == 200:
            print("✅ Server is up and reachable at", SERVER_URL)
        else:
            print("⚠️ Server responded but with error:", r.status_code)
    except Exception as e:
        print("❌ Could not connect to server:", str(e))

@app.post("/client/request")
def request_ride(user_id: str, source: str, destination: str):
    """Forward ride request to server API"""
    try:
        response = requests.post(
            f"{SERVER_URL}/request-ride",
            json={"user_id": user_id, "source": source, "destination": destination}
        )
        response.raise_for_status()
        return {"status": "success", "server_response": response.json()}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error contacting server: {str(e)}")

@app.get("/")
def root():
    return {"message": "✅ Client API is running"}
