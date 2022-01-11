from typing import Any
from src.data.database.entities import AgentTask


def validate_save_task_data(data: dict[str, Any]) -> str:
    errors = []

    seed = data.get('seed', None)
    bot = data.get('bot', None)

    if seed is None or seed == '':
        errors.append('Seed value cannot be None.')
    
    if bot is None or bot == '':
        errors.append('Bot value cannot be None.')
    
    error = ' '.join(errors)
    error = error.strip()
    
    return error
    

