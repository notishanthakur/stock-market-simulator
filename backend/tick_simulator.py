import random
import time
import asyncio
from buffer import tick_buffer

SYMBOLS = ['AAPL', 'GOOG', 'MSFT', 'TSLA', 'AMZN']

async def generate_ticks():
    while True:
        tick = {
            'symbol': random.choice(SYMBOLS),
            'price': round(random.uniform(100, 1000), 2),
            'timestamp': time.time()
        }

        tick_buffer.add_tick(tick)

        await asyncio.sleep(1)

#randomly generating data but using uniform distribution for realistic values   