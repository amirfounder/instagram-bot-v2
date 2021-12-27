from subprocess import Popen
from src.utils.subprocessing import kill_subprocess
from src.console.server.server import start_server
from src.data_manager.database import setup_database
from src.data_manager.data_syncs import sync_databases
from src.app_state import state


def run_content_builder(process_map: dict[str, Popen]):
    process = Popen('npm --prefix src/builders/content_builder run start', shell=True)
    process_map['content_builder'] = process


def run_http_listener(process_map: dict[str, Popen]):
    process = Popen("mitmdump -s src/http_listener/listener.py --set console_eventlog_verbosity=error termlog_verbosity=error", shell=True)
    process_map['http_listener'] = process


def run_console_client():
    subprocess = Popen('npm --prefix src/console/client run start', shell=True)

    state['console']['client']['is_running'] = True
    state['console']['client']['subprocess_object'] = subprocess


def run_database_setup():
    setup_database()


def run_data_syncs():
    sync_databases()


def run_console_server():
    start_server(state)


def kill_console_client(process_map: dict[str, Popen]):
    if 'console_client' not in process_map:
        process = process_map['console_client']
        kill_subprocess(process)
    

def kill_console_server(state):
    pass


def kill_http_listener(process_map: dict[str, Popen]):
    if 'http_listener' in process_map:
        process = process_map['http_listener']
        kill_subprocess(process)


def kill_content_builder(process_map: dict[str, Popen]):
    if 'content_builder' in process_map:
        process = process_map['content_builder']
        kill_subprocess(process)


def run_instagram_agent():
    pass
