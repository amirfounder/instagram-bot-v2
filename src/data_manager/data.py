from time import sleep
from src.data_manager.files import read_from_file_in_directory_recursively
from src.utils.constants import MITM_PROXY_LOGS_DIRECTORY_PATH


def sync_mitm_data_from_files_to_database():
	data = read_from_file_in_directory_recursively(MITM_PROXY_LOGS_DIRECTORY_PATH)
	print(data)


def run_data_syncs(state: dict):
	while state['data_syncs']['is_running']:
		sync_mitm_data_from_files_to_database()
		sleep(5)
