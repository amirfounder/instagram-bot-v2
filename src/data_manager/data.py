from time import sleep
from src.data_manager.files import read_from_file, read_from_files_in_directory
from src.utils.constants import MITM_PROXY_LOGS_DIRECTORY_PATH, MITM_PROXY_LOGS_SYNCED_DIRECTORY_PATH
from itertools import chain
import json


def sync_instagram_responses_from_files_to_database():
	path = MITM_PROXY_LOGS_DIRECTORY_PATH + '/instagram/json'
	data_map = read_from_files_in_directory(path)
	
	data_by_file = data_map.values()
	string_responses_by_file = [x.split('\n') for x in data_by_file]

	string_responses = list(chain(*string_responses_by_file))
	responses = []

	for string_response in string_responses:
		try:
			response = json.loads(string_response)
			responses.append(response)
		except:
			pass
	
	unsynced_responses = get_unsynced_responses(responses)
	sync_responses(unsynced_responses)


def get_unsynced_responses(responses: list[dict[str, str]]):
	unsynced_responses = []
	for response in responses:
		if not is_response_synced(response):
			unsynced_responses.append(response)
	return unsynced_responses


def is_response_synced(response: dict[str, str]):
	path = MITM_PROXY_LOGS_SYNCED_DIRECTORY_PATH + '/instagram/json/synced_timestamps.txt'
	synced_timestamps_data = read_from_file(path)
	synced_timestamps = synced_timestamps_data.split('\n')

	if ['meta'] in response and ['timestamp'] in response['meta']:
		return response['meta']['timestamp'] in synced_timestamps

	return True


def sync_responses(responses: list[dict[str, str]]):
	pass


def run_data_syncs(state: dict):
	while state['data_syncs']['is_running']:
		sync_instagram_responses_from_files_to_database()
		sleep(1)
