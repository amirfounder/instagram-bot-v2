import asyncio
from typing import Any
import websockets
import json
from websockets.legacy.server import WebSocketServerProtocol
from src.console.server.server_handlers import end_activity, start_activity


program_state = None
loop = None

async def ws_handler(websocket: WebSocketServerProtocol):
    while True:
        global program_state

        json_message: str = await websocket.recv()

        message: dict[str, Any] = json.loads(json_message)
        message_type: str = message['type']

        if message_type.lower() == 'start_activity':
            start_activity(message, program_state)
        elif message_type.lower() == 'end_activity':
            end_activity(message, program_state)


def start_server(state):
    global program_state
    global loop

    program_state = state
    loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)

    server = websockets.serve(ws_handler, "localhost", 8001)

    loop.run_until_complete(server)
    loop.run_forever()
