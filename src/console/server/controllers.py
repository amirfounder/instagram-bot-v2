from src.agents.agent import *


def handle_message(message: dict):
    message_type: str = message['type']
    message_data: dict = message['data']
    
    if message_type.lower() == 'queue_agent_task':
        queue_agent_task(message_data)
    
    if message_type.lower() == 'run_agent':
        run_agent_until_finished()
