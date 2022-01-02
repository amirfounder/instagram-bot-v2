from subprocess import Popen, PIPE
from src.utils.subprocessing import kill_subprocess
from src.console.server.server import start_server
from src.data.database import setup_database
from time import time
from src.data.data_syncs import sync_databases


def run_content_builder(state):
    popen = Popen('npm --prefix src/builders/content_builder run start', shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    state['content_builder.is_running'] = True
    state['content_builder.subprocess_object'] = popen


def run_http_listener(state):
    popen = Popen('mitmdump -s src/http_listener/listener.py --set console_eventlog_verbosity=error termlog_verbosity=error', shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    state['http_listener.is_running'] = True
    state['http_listener.subprocess_object'] = popen


def run_console_client(state):
    popen = Popen('npm --prefix src/console/client run start', shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    
    started_time = time()
    start_confirmed = False
    
    while not start_confirmed:
        output = popen.stdout.readline()
        output = output.decode('utf-8')
        output = output.removesuffix('\n')
        print(output)

        if 'Compiled successfully!' in output:
            start_confirmed = True

        if time() - started_time >= 30:
            raise TimeoutError('30 seconds have passed since starting process and no success message has been received')

    state['console.client.is_running'] = True
    state['console.client.subprocess_object'] = popen


def run_database_setup(state):
    setup_database()


def run_data_syncs(state):
    state['data_syncs.is_running'] = True
    sync_databases(state)


def run_console_server(state):
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
