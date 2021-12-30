from time import sleep

from flatdict import FlatterDict
from src.programs import run_database_setup, run_console_client, run_console_server, run_data_syncs
from src.state import state
from src.utils.threading import spawn_thread
from src.utils.utils import find_differences_between_two_flat_dicts
from copy import deepcopy, copy


def run():
    run_database_setup(state)

    spawn_thread(run_console_client, (state,))
    spawn_thread(run_console_server, (state,))
    spawn_thread(run_data_syncs, (state,))

    prev_state = deepcopy(state)
    

    while state['program_is_running']:
        adjust_programs(prev_state, state)
        prev_state = deepcopy(state)
        sleep(3)


def adjust_programs(prev_state: FlatterDict, current_state: FlatterDict):
    prev_state_set = set(prev_state.items())
    current_state_set = set(current_state.items())

    diff = current_state_set ^ prev_state_set
    diff = dict(diff)

    diffs2 = find_differences_between_two_flat_dicts(prev_state, current_state)

    pass
