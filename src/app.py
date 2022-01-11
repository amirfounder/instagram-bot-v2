import os
import signal
from src.data.database.entities import ProgramProcess
from src.utils.wrappers.threading import spawn_thread
from src.console.server.app import start_server
from src.data.database import setup_database
from src.data.data_syncs import sync_databases
from src.data.repository import save_program_process, get_all_program_processes_by_column, update_program_process
from src.utils.constants import CONSOLE_CLIENT_SHELL_SCRIPT, CONTENT_BUILDER_SHELL_SCRIPT, HTTP_LISTENER_SHELL_SCRIPT
from src.utils.wrappers.subprocessing import spawn_subprocess


def run():
    
    run_signal_registration()
    run_database_setup()

    program_process = ProgramProcess()
    program_process.pid = os.getpid()
    program_process.name = 'MainProcess'
    program_process.is_open = True
    save_program_process(program_process)

    spawn_thread(run_data_syncs)
    spawn_thread(run_console_client)
    spawn_thread(run_console_server)
    spawn_thread(run_http_listener)

    while True:
        pass


def run_signal_registration():

    def handler(_, __):
        print('Shutting down application')
        
        open_processes_in_db: list[ProgramProcess]
        open_processes_in_db = get_all_program_processes_by_column('is_open', True)
        
        for open_process in open_processes_in_db:
            open_process.is_open = False
            update_program_process(open_process)
        
        quit(1)

    signal.signal(signal.SIGINT, handler)


def run_database_setup():
    setup_database()


def run_content_builder():
    popen = spawn_subprocess(CONTENT_BUILDER_SHELL_SCRIPT)
    program_process = ProgramProcess()
    program_process.pid = popen.pid
    program_process.name = 'ContentBuilder'
    program_process.is_open = True
    save_program_process(program_process)


def run_data_syncs():
    sync_databases()


def run_console_client():
    popen = spawn_subprocess(CONSOLE_CLIENT_SHELL_SCRIPT)
    program_process = ProgramProcess()
    program_process.pid = popen.pid
    program_process.name = 'ConsoleClient'
    program_process.is_open = True
    save_program_process(program_process)


def run_console_server():
    start_server()


def run_http_listener():
    popen = spawn_subprocess(HTTP_LISTENER_SHELL_SCRIPT)
    program_process = ProgramProcess()
    program_process.pid = popen.pid
    program_process.name = 'HttpListener'
    program_process.is_open = True
    save_program_process(program_process)
