from server import manager
from fastapi import WebSocket, WebSocketDisconnect


def send_personal_message(message: str, websocket: WebSocket):
    manager.send_personal_message(message, websocket)