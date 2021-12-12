import os
from multiprocessing import Process

from src.data_manager.database import setup


def run():

	setup()

	processes: list[Process] = []
	drivers: list[function] = [
        # run_data_manager,
        # run_http_listener,
        # run_interaction_logger,
        # run_bot_builder,
        # run_content_builder,
        # run_instagram_agent
    ]

	for driver in drivers:
		process = Process(target=driver)
		processes.append(process)

	for process in processes:
		process.start()

	for process in processes:
		process.join()


def run_data_manager():
    pass


def run_http_listener():
    os.system("mitmdump -s src/http_listener/listener.py --set console_eventlog_verbosity=error termlog_verbosity=error")


def run_interaction_logger():
    pass


def run_bot_builder():
    pass


def run_content_builder():
    os.system('npm start')


def run_instagram_agent():
    pass
