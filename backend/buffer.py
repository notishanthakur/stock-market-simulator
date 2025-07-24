from collections import deque
import threading

class TickBuffer:
    def __init__(self, max_len=100):
        self.buffer = deque(maxlen=max_len)
        self.lock = threading.Lock()

    def add_tick(self, tick):
        with self.lock:
            self.buffer.append(tick)

    def get_ticks(self):
        with self.lock:
            return list(self.buffer)

tick_buffer = TickBuffer()