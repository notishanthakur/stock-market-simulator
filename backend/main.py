from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tick_simulator import generate_ticks, generate_candlesticks
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/candles")
def get_candles():
    ticks = generate_ticks(100)
    candles = generate_candlesticks(ticks)
    return candles

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)