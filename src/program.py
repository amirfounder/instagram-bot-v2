import os
from multiprocessing import Process, Manager
from typing import Any

from src.data_manager.database import setup as setup_database
from src.console import run_client as run_console_client, run_server as run_console_server


def run():
    """Thread safe variables. Try this!
    """
    manager = Manager()
    state = manager.dict()

    state['manager'] = manager
    state['processes'] = manager.dict()
    state['is_program_running'] = True

    """Setup database. Register entities and sync tables
    """
    setup_database()

    """
    Setup Console
    TODO: Pass thread safe variable to ensure client and server successfully started. Timeout=15 seconds
    """
    state['processes']['run_console_server'] = spawn_process(run_console_server).pid
    state['processes']['run_console_client'] = spawn_process(run_console_client).pid

    """
    Setup HTTP Listener
    TODO: Maybe move this into the main event loop
    """
    # config.state['processes']['run_http_listener'] = spawn_process(run_http_listener)

    while state['is_program_running']:
        """Main event loop. User defined actions will update 
        """
        pass


def setup_content_builder():
    os.system('npm --prefix src/builders/content_builder run start')


def run_http_listener():
    os.system("mitmdump -s src/http_listener/listener.py --set console_eventlog_verbosity=error termlog_verbosity=error")


def run_content_builder():
    os.system('')


def run_instagram_agent():
    pass


def run_console():
    pass


def run_multiple_processes(drivers: list):
    processes: list[Process] = []

    for driver in drivers:
        process = Process(target=driver)
        processes.append(process)

    for process in processes:
        process.start()

    return processes


def spawn_process(target, args: tuple[Any] = ())-> Process:
    process = Process(target=target, args=args)
    process.start()

    return process
