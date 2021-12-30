from time import sleep

from flatdict import FlatterDict
from src.programs import run_database_setup, run_console_client, run_console_server, run_data_syncs
from src.state import state
from src.utils.threading import spawn_thread
from src.utils.utils import get_differences_from_prev_state, copy_state



def run():
    run_database_setup(state)

    spawn_thread(run_console_client, (state,))
    spawn_thread(run_console_server, (state,))
    spawn_thread(run_data_syncs, (state,))

    prev_state = state

    while state['program_is_running']:
        adjust_programs(prev_state, state)
        
        prev_state = copy_state(state)
        sleep(1)


def adjust_programs(prev_state: FlatterDict, current_state: FlatterDict):
    diffs = get_differences_from_prev_state(prev_state, current_state)
    print(prev_state['instagram_agent.tasks.research_hashtags.is_running'])
    print(current_state['instagram_agent.tasks.research_hashtags.is_running'])
    print(diffs)
