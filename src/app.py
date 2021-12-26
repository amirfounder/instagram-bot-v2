from time import sleep
from src.programs import run_database_setup, run_console_client, run_console_server, run_data_syncs
from src.utils.threading import spawn_thread
from src.app_state import state


def run():

    run_database_setup()
    spawn_thread(run_console_client)
    spawn_thread(run_console_server)
    spawn_thread(run_data_syncs)

    prev_state = state

    while state['program_is_running']:
        adjust_programs(prev_state, state)
        prev_state = state
        sleep(1)


def adjust_programs(prev_state, current_state):
    pass
