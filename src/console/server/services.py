from typing import Any


def start_program(message: dict[str, Any], state: dict[str, Any]):
    program = message['program']
    task = message['task']

    if program == 'instagram_agent':
        if task == 'research_hashtags':
        
            seed_hashtag = message['seed_hashtag']
            start_instagram_agent_hashtag_research_program(seed_hashtag, state)


def start_instagram_agent_hashtag_research_program(seed_hashtag:str, state: dict[str, Any]):
    state['instagram_agent.is_running'] = True
    state['instagram_agent.tasks.research_hashtags.is_running'] = True
    state['instagram_agent.tasks.research_hashtags.seed_hashtag'] = seed_hashtag
    print('started instagram agent hashtag research program')


def end_program(message: dict[str, Any], state: dict[str, Any]):
    program = message['program']
    task = message['task']

    if program == 'instagram_agent':
        if task == 'research_hashtags':

            end_instagram_agent_hashtag_research_program(state)


def end_instagram_agent_program(state: dict[str, Any]):
    state['instagram_agent.is_running'] = False


def end_instagram_agent_hashtag_research_program(state: dict[str, Any]):
    pass
