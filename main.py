from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Mini Backend")

@app.get("/")
def home():
    return {"message": "Server is alive", "time": datetime.now().isoformat()}

@app.get("/api/status")
def status():
    return {"status": "ok", "service": "mini-backend", "version": "1.0"}

@app.get("/api/greet/{name}")
def greet(name: str, loud: bool = False):
    message = f"Hello, {name}!"
    return {"message": message.upper() if loud else message}

@app.post("/api/echo")
def echo(payload: dict):
    return {"you_sent": payload, "received_at": datetime.now().isoformat()}