from src.utils.dtos.agent_dtos import build_research_hashtags_task_dto, build_research_users_task_dto
from src.data.database.utils import convert_entity_to_dict
# from src.data.repository import save_task


def run_agent_until_finished():
    pass


def queue_agent_task(task_data: dict):
    name: str
    name = task_data['name']

    if name.lower() == 'research_hashtags':
        task = build_research_hashtags_task_dto(task_data)
    
    if name.lower() == 'research_users':
        task = build_research_users_task_dto(task_data)
    
    # task = save_task(task)
    task = convert_entity_to_dict(task)
