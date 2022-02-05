import os
import signal
from src.data.database.entities import AppProcess
from src.utils.utils import build_datetimestamp
from src.utils.wrappers.threading import spawn_thread
from src.console.server.app import start_server
from src.data.database import setup_database
from src.data.data_syncs import sync_databases
from src.data.repository import save_app_process, get_all_app_processes_by_column, update_app_process
from src.utils.constants import CONSOLE_CLIENT_SHELL_SCRIPT, CONTENT_BUILDER_SHELL_SCRIPT, HTTP_LISTENER_SHELL_SCRIPT
from src.utils.wrappers.subprocessing import spawn_subprocess


def run():
    
    run_signal_registration()
    run_database_setup()

    app_process = AppProcess()
    app_process.pid = os.getpid()
    app_process.name = 'MainProcess'
    app_process.is_open = True
    save_app_process(app_process)

    spawn_thread(run_data_syncs)
    spawn_thread(run_console_client)
    spawn_thread(run_console_server)
    spawn_thread(run_http_listener)

    while True:
        pass


def run_signal_registration():

    def handler(_, __):
        print('Shutting down application')
        
        open_processes_in_db: list[AppProcess]
        open_processes_in_db = get_all_app_processes_by_column('is_open', True)
        
        for open_process in open_processes_in_db:
            open_process.is_open = False
            update_app_process(open_process)
        
        quit(1)

    signal.signal(signal.SIGINT, handler)


def run_database_setup():
    print('{} : Running database setup'.format(build_datetimestamp()))
    setup_database()
    print('{} : Database setup complete'.format(build_datetimestamp()))


def run_content_builder():
    popen = spawn_subprocess(CONTENT_BUILDER_SHELL_SCRIPT)
    app_process = AppProcess()
    app_process.pid = popen.pid
    app_process.name = 'ContentBuilder'
    app_process.is_open = True
    save_app_process(app_process)


def run_data_syncs():
    print('{} : Starting data syncs'.format(build_datetimestamp()))
    sync_databases()


def run_console_client():
    popen = spawn_subprocess(CONSOLE_CLIENT_SHELL_SCRIPT)
    app_process = AppProcess()
    app_process.pid = popen.pid
    app_process.name = 'ConsoleClient'
    app_process.is_open = True
    save_app_process(app_process)


def run_console_server():
    start_server()


def run_http_listener():
    popen = spawn_subprocess(HTTP_LISTENER_SHELL_SCRIPT)
    app_process = AppProcess()
    app_process.pid = popen.pid
    app_process.name = 'HttpListener'
    app_process.is_open = True
    save_app_process(app_process)
