import random
import time

def generate_ticks(num_ticks=50, base_price=100.0, volatility=1.0):
    ticks = []
    price = base_price
    for _ in range(num_ticks):
        price += random.uniform(-volatility, volatility)
        ticks.append(round(price, 2))
    return ticks

def generate_candlesticks(ticks, ticks_per_candle=5):
    candles = []
    timestamp = time.time()
    for i in range(0, len(ticks), ticks_per_candle):
        chunk = ticks[i:i+ticks_per_candle]
        if len(chunk) < ticks_per_candle:
            continue
        candles.append({
            "time": timestamp + i,
            "open": chunk[0],
            "high": max(chunk),
            "low": min(chunk),
            "close": chunk[-1],
        })
    return candles