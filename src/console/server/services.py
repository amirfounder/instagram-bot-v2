from typing import Any
from src.console.server.validation import validate_save_task_data
from src.data.database.entities import AgentTask, AppProgram
from src.data.repository import save_agent_task, save_app_program
from src.utils.constants import RUNNING


def save_task_service(data: dict):

    error = validate_save_task_data(data)
    if error != '':
        print('There was a validation error with the task to save: {}'.format(error))
        return

    task = AgentTask()

    name = data.get('name')
    status = data.get('status')
    seed = data.get('seed')
    bot = data.get('bot')

    task.name = name
    task.status = status
    task.args = 'seed={} bot={}'.format(seed, bot)

    save_agent_task(task)


def start_program_service(data: dict):
    name = data.get('name')

    app_program = AppProgram()

    app_program.name = name
    app_program.status = RUNNING

    save_app_program(app_program)


def start_program(data: dict[str, Any], state: dict[str, Any]):
    program = data['program']
