from typing import Any
from src.agents.agent import *
from websockets.server import WebSocketServerProtocol
from json import loads


async def ws_controller(websocket: WebSocketServerProtocol):
    while True:
        json_message: str = await websocket.recv()
        message: dict[str, Any] = loads(json_message)
        
        message_type: str = message['type']
        message_data: dict = message['data']

        if message_type.lower() == 'queue_agent_task':
            queue_agent_task(message_data)
        
        if message_type.lower() == 'run_agent':
            run_agent_until_finished()
