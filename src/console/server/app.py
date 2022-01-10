from typing import Any
from websockets.server import WebSocketServer
from src.console.server.controllers import ws_controller
from asyncio import new_event_loop, set_event_loop
from websockets import serve



def start_server():
    loop = new_event_loop()
    set_event_loop(loop)

    ws_server: WebSocketServer
    ws_server = serve(ws_controller, '127.0.0.1', 8001)

    try:
        loop.run_until_complete(ws_server)
        loop.run_forever()
    finally:
        ws_server.close()
        loop.stop()
