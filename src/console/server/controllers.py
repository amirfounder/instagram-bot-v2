from typing import Any

from src.controllers.controller import *
from websockets.server import WebSocketServerProtocol
from json import loads
from src.console.server.services import save_task_service, start_program_service


async def ws_controller(websocket: WebSocketServerProtocol):
    while True:
        json_message: str = await websocket.recv()
        print('Websockets Server received the following message: {}'.format(json_message))
        
        message: dict[str, Any] = loads(json_message)
        message_type: str = message.get('type', None)
        message_method: dict = message.get('method', None)
        message_data: dict = message.get('data', None)

        if message_type.lower() == 'task':
            if message_method.lower() == 'save':
                save_task_service(message_data)
        
        if message_type.lower() == 'program':
            if message_method.lower() == 'start':
                start_program_service(message_data)
