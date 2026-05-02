import os
from fastapi import FastAPI, Request
from binance.client import Client

app = FastAPI()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)

@app.get("/")
def home():
    return {"status": "bot running"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    symbol = data.get("symbol")
    signal = data.get("signal")

    return {
        "message": "Signal reçu",
        "symbol": symbol,
        "signal": signal
    }