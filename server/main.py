# server/main.py
from fastapi import FastAPI
from server.routes import rides

app = FastAPI()

# ✅ Root health check
@app.get("/")
def root():
    return {"message": "🚀 Server is running fine!"}

app.include_router(rides.router)
