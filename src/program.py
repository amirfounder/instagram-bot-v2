import os
from multiprocessing import Process, Manager
from multiprocessing.process import AuthenticationString
from typing import Any, Callable, Mapping, Tuple

from src.data_manager.database import setup as setup_database
from src.console import run_client as run_console_client, run_server as run_console_server


def run():
    """Thread safe variables
    """
    manager = Manager()

    is_running = manager.Value('b', True)
    processes: dict[str, Process] = manager.dict()

    """Setup database. Register entities and sync tables
    """
    setup_database()

    """
    Setup Console
    TODO: Pass thread safe variable to ensure client and server successfully started. Timeout=15 seconds
    """
    processes['console_client'] = spawn_process(run_console_client)
    processes['console_server'] = spawn_process(run_console_server)

    """
    Setup HTTP Listener
    TODO: Maybe move this into the main event loop
    """
    processes['http_listener'] = spawn_process(setup_http_listener)

    while is_running.value:
        """Main event loop. User defined actions will update 
        """
        pass


def setup_http_listener():
    os.system("mitmdump -s src/http_listener/listener.py --set console_eventlog_verbosity=error termlog_verbosity=error")


def setup_content_builder():
    os.system('npm --prefix src/builders/content_builder run start')


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


def spawn_process(target, args: tuple[Any] = ()):
    process = Process(target=target, args=args)
    process.start()

    return process


class CustomProcess(Process):
    def __init__(
            self,
            group: None = ...,
            target: Callable[..., Any] | None = ...,
            name: str | None = ...,
            args: Tuple[Any, ...] = ...,
            kwargs: Mapping[str, Any] = ..., *,
            daemon: bool | None = ...) -> None:
        super().__init__(
            group=group,
            target=target,
            name=name,
            args=args,
            kwargs=kwargs,
            daemon=daemon)

    def __getstate__(self):
        state = self.__dict__.copy()
        conf = state['_config']
        if 'authkey' in conf:
            conf['authkey'] = bytes(conf['authkey'])
        return state
    
    def __setstate__(self, state):
        state['_config']['authkey'] = AuthenticationString(
            state['_config']['authkey']
        )
        self.__dict__.update(state)