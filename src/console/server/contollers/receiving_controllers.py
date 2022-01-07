from src.utils.utils import try_parse_json


def get_all_processes():
    pass


def start_process():
    pass


def end_process():
    pass


def get_all_task_templates():
    pass


def get_all_tasks():
    pass


def get_all_task_results():
    pass


def start_task(json_object: str):
    parsed_object = try_parse_json(json_object)
    task_name = parsed_object['task']

    if task_name == 'research_hashtags':
        start_task_research_hashtags(parsed_object)


def start_task_research_hashtags(data: dict):
    seed_hashtag = data['seed_hashtag']
    account = data['account']


def build_agent_task_dto(object: dict):
    return {
        'seed_hashtag': object.get('seed_hashtag', None),
        'account': object.get('account', None)
    }