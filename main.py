import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from emotions import get_bbox_prediction

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_json(self, message: dict, websocket: WebSocket):
        await websocket.send_json(message)


manager = ConnectionManager()


@app.get("/")
async def get():
    return {200: "OK"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            image_b64 = data['data']['image'].split(',')[1]

            emotions_predictions = get_bbox_prediction(image_b64)
            await manager.send_json(emotions_predictions, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
