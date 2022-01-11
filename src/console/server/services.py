from logging import error
from typing import Any

from websockets.legacy.server import WebSocketServerProtocol
from src.console.server.validation import validate_save_task_data
from src.data.database.entities import AgentTask
from src.data.repository import save_agent_task


def save_task_service(websocket: WebSocketServerProtocol, data: dict):

    error = validate_save_task_data(data)
    if error != '':
        print('There was a validation error with the task to save: {}'.format(error))
        return

    task = AgentTask()

    name = data.get('name', None)
    status = data.get('status', None)
    seed = data.get('seed', None)
    bot = data.get('bot', None)

    task.name = name
    task.status = status
    task.args = 'seed={} bot={}'.format(seed, bot)

    save_agent_task(task)


def get_all_processes():
    pass


def start_process():
    pass


def end_process():
    pass


def get_all_tasks():
    pass


def get_all_task_results():
    pass


def start_program(data: dict[str, Any], state: dict[str, Any]):
    program = data['program']


def end_program(data: dict[str, Any], state: dict[str, Any]):
    program = data['program']

