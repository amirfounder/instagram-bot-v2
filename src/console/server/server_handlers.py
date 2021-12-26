from typing import Any


def start_program(message: dict[str, Any], program_state: dict[str, Any]):
    program = message['program']
    task = message['task']

    if program == 'instagram_agent':
        if task == 'research_hashtags':
        
            seed_hashtag = message['seed_hashtag']
            start_instagram_agent_hashtag_research_program(seed_hashtag, program_state)


def start_instagram_agent_hashtag_research_program(seed_hashtag:str, program_state: dict[str, Any]):
    program_state['instagram_agent']['is_running'] = True
    program_state['instagram_agent']['tasks']['research_hashtags']['is_running'] = False
    program_state['instagram_agent']['tasks']['research_hashtags']['seed_hashtag'] = seed_hashtag


def end_program(message: dict[str, Any], program_state: dict[str, Any]):
    program = message['program']
    task = message['task']

    if program == 'instagram_agent':
        if task == 'research_hashtags':

            end_instagram_agent_hashtag_research_program(program_state)


def end_instagram_agent_program(program_state: dict[str, Any]):
    program_state['instagram_agent']['is_running'] = False


def end_instagram_agent_hashtag_research_program(program_state: dict[str, Any]):
    pass
