from fastapi import FastAPI , WebSocket, WebSocketDisconnect
from connection_manager import ConnectionManager

app = FastAPI()

manager = ConnectionManager()


@app.websocket("/chat/{room}")
async def websocket_chat(websocket: WebSocket, room: str):
    await manager.connect(websocket,room)

    try:
        while True:
            data = await websocket.receive_text()

            await manager.broadcast(f"{room}: {data}", room)
    except WebSocketDisconnect:
        manager.disconnect(
            websocket,
            room
        )
        print("Client Disconnected")