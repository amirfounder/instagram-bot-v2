import subprocess

from os import kill
from subprocess import Popen

from src.utils.threading import spawn_thread
from src.console.server import run_console_server
from src.data_manager.database import setup_database
from src.data_manager.data_syncs import run_data_syncs

import signal


def run():

    state = {}
    state['program_is_running'] = True
    state['process_map'] = {}

    setup_database()
    spawn_thread(run_console_client, (state['process_map'],))
    spawn_thread(run_console_server, (state['process_map'],))
    spawn_thread(run_console_server, (state['process_map'],))
    spawn_thread(run_console_server, (state, ))
    spawn_thread(run_data_syncs)

    while state['main_running']:
        pass

    kill_console_client(state['process_map'])
    kill_content_builder(state['process_map'])
    kill_http_listener(state['process_map'])


def run_content_builder(process_map: dict[str, Popen]):
    process = subprocess.Popen('npm --prefix src/builders/content_builder run start', shell=True)
    process_map['content_builder'] = process


def run_http_listener(process_map: dict[str, Popen]):
    process = subprocess.Popen("mitmdump -s src/http_listener/listener.py --set console_eventlog_verbosity=error termlog_verbosity=error", shell=True)
    process_map['http_listener'] = process


def run_console_client(process_map: dict[str, Popen]):
    process = subprocess.Popen('npm --prefix src/console/client run start', shell=True)
    process_map['console_client'] = process


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


def kill_subprocess(process: Popen):
    pid = process.pid
    kill(pid, signal.CTRL_C_EVENT)


def run_instagram_agent():
    pass
