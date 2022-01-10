from src.data.database.entities import XProcess
from src.utils.wrappers.threading import spawn_thread
from src.console.server.app import start_server
from src.data.database import setup_database
from src.data.data_syncs import sync_databases
from src.data.repository import save_x_process
from src.utils.constants import CONSOLE_CLIENT_SHELL_SCRIPT, CONTENT_BUILDER_SHELL_SCRIPT, HTTP_LISTENER_SHELL_SCRIPT
from src.utils.wrappers.subprocessing import spawn_subprocess
from multiprocessing import current_process



def run():
    main_process = current_process()

    x_process = XProcess()
    x_process.pid = main_process.pid
    x_process.name = main_process.name
    x_process.is_open = True

    save_x_process(x_process)

    run_database_setup()
    spawn_thread(run_data_syncs)
    spawn_thread(run_console_client)
    spawn_thread(run_console_server)
    spawn_thread(run_http_listener)


def run_database_setup():
    setup_database()


def run_content_builder():
    popen = spawn_subprocess(CONTENT_BUILDER_SHELL_SCRIPT)
    pid = popen.pid


def run_data_syncs():
    sync_databases()


def run_console_client():
    spawn_subprocess(CONSOLE_CLIENT_SHELL_SCRIPT)


def run_console_server():
    start_server()


def run_http_listener():
    spawn_subprocess(HTTP_LISTENER_SHELL_SCRIPT)
