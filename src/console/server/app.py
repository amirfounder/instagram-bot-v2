from typing import Any
from websockets.server import WebSocketServerProtocol, WebSocketServer
import asyncio
import websockets
import json

from src.console.server.controllers import handle_message


async def ws_handler(websocket: WebSocketServerProtocol):
    while True:
        json_message: str = await websocket.recv()
        message: dict[str, Any] = json.loads(json_message)
        handle_message(message)


def start_server():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    ws_server: WebSocketServer = websockets.serve(ws_handler, 'localhost', 8001)

    try:
        loop.run_until_complete(ws_server)
        loop.run_forever()
    finally:
        ws_server.close()
        loop.stop()
