from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from connection_manager import ConnectionManager

app = FastAPI()

manager = ConnectionManager()

@app.websocket("/chat")
async def websocket_chat(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

            await manager.broadcast(f"Message: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Client disconnected")