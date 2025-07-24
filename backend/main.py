from fastapi import FastAPI, WebSocket
import uvicorn
from tick_simulator import generate_ticks
from buffer import tick_buffer
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(generate_ticks())

@app.get("/")
async def root():
    return {"message": "Tick server is running."}

@app.websocket("/ws/ticks")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        ticks = tick_buffer.get_ticks()
        await websocket.send_json(ticks)
        await asyncio.sleep(1)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)