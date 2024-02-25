import base64
import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from emotions import get_bbox_prediction
import numpy as np
import cv2

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_text(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def send_json(self, message: dict, websocket: WebSocket):
        await websocket.send_json(message)


manager = ConnectionManager()


@app.get("/")
async def get():
    return {200: "OK"}


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            imageByt64 = data['data']['image'].split(',')[1]

            nparr = np.fromstring(base64.b64decode(imageByt64), np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            emotions_predictions = get_bbox_prediction(img)

            await manager.send_json(emotions_predictions, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
