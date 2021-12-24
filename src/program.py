import subprocess


from subprocess import Popen
from multiprocessing import Manager

from src.utils.processing import spawn_process
from src.console.server import run_console_server
from src.data_manager.database import setup_database
from src.data_manager.data_syncs import run_data_syncs

from time import sleep

from threading import Thread


def run():

    # t1 = Thread(target=run_http_listener)
    t2 = Thread(target=run_console_client)
    # t3 = Thread(target=run_content_builder)
    # t4 = Thread(target=setup_database)

    # t1.start()
    t2.start()
    # t3.start()
    # t4.start()
    # manager = Manager()
    # state = manager.dict()

    # state['is_program_running'] = True
    # state['processes'] = manager.dict()

    # setup_database()

    # state['console_server'] = manager.dict()
    # state['console_client'] = manager.dict()
    # state['http_listener'] = manager.dict()
    # state['instagram_agent'] = manager.dict()
    # state['data_syncs'] = manager.dict()

    # state['console_server']['pid'] = spawn_process(run_console_server, (state,)).pid
    # state['console_client']['pid'] = spawn_process(run_console_client).pid
    # state['http_listener']['pid'] = spawn_process(run_http_listener).pid
    # state['instagram_agent']['pid'] = spawn_process(run_instagram_agent, (state,)).pid
    # state['data_syncs']['pid'] = spawn_process(run_data_syncs, (state,)).pid

    # state['console_server']['is_running'] = True
    # state['console_client']['is_running'] = True
    # state['http_listener']['is_running'] = True
    # state['instagram_agent']['is_running'] = True
    # state['data_syncs']['is_running'] = True

    # while state['is_program_running']:
    #     pass


def run_content_builder():
    subprocess.Popen('npm --prefix src/builders/content_builder run start', shell=True)


def run_http_listener():
    subprocess.Popen("mitmdump -s src/http_listener/listener.py --set console_eventlog_verbosity=error termlog_verbosity=error", shell=True)


def run_console_client():
    process = subprocess.Popen('npm --prefix src/console/client run start', shell=True)
    for i in range(10):
        print(10 - i)
        sleep(1)
    process.communicate('.exit')


def run_instagram_agent():
    pass
