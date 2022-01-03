import asyncio
from typing import Any
import websockets
import json
from websockets.server import WebSocketServerProtocol, WebSocketServer
from src.console.server.services import end_program, start_program


async def ws_handler(websocket: WebSocketServerProtocol, state):
    while True:
        json_message: str = await websocket.recv()
        message: dict[str, Any] = json.loads(json_message)
        message_type: str = message['type']

        if message_type.lower() == 'start_program':
            start_program(message, state)
        elif message_type.lower() == 'end_program':
            end_program(message, state)


def start_server(state):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    ws_server: WebSocketServer = websockets.serve(
        lambda x: ws_handler(x, state),
        'localhost',
        8001
    )

    try:
        loop.run_until_complete(ws_server)
        loop.run_forever()
    finally:
        ws_server.close()
        loop.stop()