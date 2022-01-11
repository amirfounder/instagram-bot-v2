from typing import Any

from websockets.legacy.protocol import WebSocketCommonProtocol
from src.agents.agent import *
from websockets.server import WebSocketServerProtocol
from json import loads
from src.console.server.services import save_task_service


async def ws_controller(websocket: WebSocketServerProtocol):
    while True:
        json_message: str = await websocket.recv()
        print('Websockets Server received the following message: {}'.format(json_message))
        
        message: dict[str, Any] = loads(json_message)
        message_type: str = message['type']
        message_method: dict = message['method']
        message_data: dict = message['data']

        if message_type.lower() == 'task':
            if message_method.lower() == 'save':
                save_task_service(websocket, message_data)
        
        if message_type.lower() == 'program':
            pass
