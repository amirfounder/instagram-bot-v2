import asyncio
import websockets
from websockets.legacy.server import WebSocketServerProtocol


def handle_message(message: str):
    pass


async def handle_event(websocket: WebSocketServerProtocol):
    while True:
        print(websocket)
        message = await websocket.recv()
        print('server received a message: {}'.format(message))


async def start_server():
    print('starting console server')
    async with websockets.serve(handle_event, "localhost", 8001):
        await asyncio.Future()
    

def run_console_server():
    asyncio.run(start_server())
