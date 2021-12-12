import os
from multiprocessing import Process, Value
from typing import Any

from src.data_manager.database import setup as setup_database
from src.console import setup_client as setup_console_client, setup_server as setup_console_server


"""Thread safe variables
"""
is_running: Value = Value('b', True)


def run():

    """Setup database. Register entities and sync tables
    """
    setup_database()

    """
    Setup Console
    TODO: Pass thread safe variable to ensure client and server successfully started. Timeout=15 seconds
    """
    spawn_process(setup_console_client)
    spawn_process(setup_console_server)

    """
    Runs the console awaiting user input
    TODO: Pass thread safe variables which will act as the user's actions / inputs
    """
    spawn_process(run_console)

    """
    Setup HTTP Listener
    TODO: Maybe move this into the main event loop
    """
    spawn_process(setup_http_listener)

    while is_running.value:
        """Main event loop. User defined actions will update 
        """
        pass


def setup_http_listener():
    os.system("mitmdump -s src/http_listener/listener.py --set console_eventlog_verbosity=error termlog_verbosity=error")


def setup_content_builder():
    os.system('npm run start-react')


def run_content_builder():
    pass


def run_instagram_agent():
    pass


def run_console():
    pass


def run_multiple_processes(drivers: list[function], blocking: bool = False):
    processes: list[Process] = []

    for driver in drivers:
        process = Process(target=driver)
        processes.append(process)

    for process in processes:
        process.start()

    if blocking:
        for process in processes:
            process.join()


def spawn_process(target, args: tuple(Any) = None, blocking: bool = False):
    p = Process(target=target)
    p.start()

    if blocking:
        p.join()
