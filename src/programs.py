from subprocess import Popen, PIPE
from src.utils.wrappers.subprocessing import kill_subprocess
from src.console.server.app import start_server
from src.data.database import setup_database
from src.data.data_syncs import sync_databases
from src.utils.constants import CONSOLE_CLIENT_SHELL_SCRIPT, CONTENT_BUILDER_SHELL_SCRIPT, HTTP_LISTENER_SHELL_SCRIPT


def run_content_builder(state):
    popen = Popen(CONTENT_BUILDER_SHELL_SCRIPT, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    state['content_builder.is_running'] = True
    state['content_builder.subprocess_object'] = popen


def run_http_listener(state):
    popen = Popen(HTTP_LISTENER_SHELL_SCRIPT, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    state['http_listener.is_running'] = True
    state['http_listener.subprocess_object'] = popen
    start_confirmed = False

    while not start_confirmed:

        output = popen.stdout.readline()
        output = output.decode('utf-8')
        output = output.removesuffix('\n')
        print('Console Client STDOUT >> {}'.format(output))

        if 'Proxy server listening at' in output:
            start_confirmed = True
            print('Successfully started <HTTP Listener>')
            break

    state['http_listener.is_running'] = True
    state['http_listener.subprocess_object'] = popen


def run_console_client(state):
    popen = Popen(CONSOLE_CLIENT_SHELL_SCRIPT, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    start_confirmed = False
    
    while not start_confirmed:
        output = popen.stdout.readline()
        output = output.decode('utf-8')
        output = output.removesuffix('\n')
        print('Console Client STDOUT >> {}'.format(output))

        if 'Compiled successfully!' in output:
            start_confirmed = True
            print('Successfully started <Console Client>')
            break

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
