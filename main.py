from fastapi import FastAPI # type: ignore
from server.routes import rides
 # type: ignore

app = FastAPI()

# 🔹 Health check / ping route
@app.post("/ping")
def ping(data: dict):
    if data.get("data") == "ping":
        return {"response": "pong"}
    return {"response": "invalid"}

# Include your rides router
app.include_router(rides.router)