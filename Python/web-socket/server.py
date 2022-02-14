from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from connection_manager import ConnectionManager
manager = ConnectionManager()

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_name = '${Date.now()}';
            document.querySelector("#ws-id").textContent = client_name;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_name}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.get("/html")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{client_name}")
async def websocket_endpoint(websocket: WebSocket, client_name: str = None, broadcast: bool = False):
    await manager.connect(websocket, client_name)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received message from {client_name}: {data}")
            await manager.send_personal_message(f"{client_name}: {data}", websocket)
            if broadcast:
                await manager.broadcast(f"Client #{client_name} says: {data}")

    except WebSocketDisconnect:

        manager.disconnect(websocket)

        await manager.broadcast(f"Client #{client_name} left the chat")
