from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .tick_simulator import generate_ticks, generate_candlesticks
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def get_index():
    return FileResponse("frontend/index.html")

base_prices = {
    "BHEL": 250.0
}

@app.get("/latest-candle/{symbol}")
def get_latest_candle(symbol: str):
    symbol = symbol.upper()
    if symbol not in base_prices:
        return {"error": "Unknown stock symbol"}
    ticks = generate_ticks(5, base_price=base_prices[symbol])
    candles = generate_candlesticks(ticks)
    if candles:
        return candles[-1]
    return {}


@app.get("/candles/{symbol}")
def get_candles(symbol: str):
    symbol = symbol.upper()
    if symbol not in base_prices:
        return {"error": "Unknown stock symbol"}
    ticks = generate_ticks(100, base_price=base_prices[symbol])
    candles = generate_candlesticks(ticks)
    return candles

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)