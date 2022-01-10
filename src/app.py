from time import sleep

from src.programs import *
from src.state import state
from src.utils.wrappers.threading import spawn_thread
from src.utils.utils import get_updated_values, copy_state



def run():
    run_database_setup(state)

    spawn_thread(run_data_syncs, (state,))
    spawn_thread(run_console_client, (state,))
    spawn_thread(run_console_server, (state,))
    spawn_thread(run_http_listener, (state,))

    prev_state = copy_state(state)

    while state['program_is_running']:

        updated_values = get_updated_values(prev_state, state)

        if '' in updated_values:
            pass

        prev_state = copy_state(state)
        sleep(.1)
