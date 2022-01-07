def build_research_hashtags_task_dto(object: dict) -> dict:
    return {
        'name': 'research_hashtags',
        'seed_hashtag': object.get('seed_hashtag', None),
        'account': object.get('account', None)
    }


def build_research_users_task_dto(object: dict) -> dict:
    return {
        'name': 'research_users'
    }
