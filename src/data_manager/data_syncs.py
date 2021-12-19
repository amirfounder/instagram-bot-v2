from time import sleep
from src.data_manager.files import convert_data_map_to_map, read_from_file, read_from_files_in_directory
from src.utils.constants import MITM_PROXY_INSTAGRAM_JSON_RESPONSES_LOGS_DIRECTORY_PATH, MITM_PROXY_INSTAGRAM_JSON_RESPONSES_SYNCED_LOGS_DIRECTORY_PATH
from src.utils.utils import try_parse_json
from itertools import chain


def sync_instagram_responses_from_files_to_database():
    data_map = read_from_files_in_directory(MITM_PROXY_INSTAGRAM_JSON_RESPONSES_LOGS_DIRECTORY_PATH)
    data = convert_data_map_to_map(data_map)
    string_responses = data.split('\n')

    responses = []
    for string_response in string_responses:
        response = try_parse_json(string_response)
        if response is not None:
            responses.append(response)

    responses = [
        x for x in responses if 'meta' in x and 'timestamp' in x['meta']]

    unsynced_responses = get_unsynced_responses(responses)
    sync_responses(unsynced_responses)


def get_unsynced_responses(responses: list[dict[str, str]]):
    unsynced_responses = []
    for response in responses:
        if not is_response_synced(response):
            unsynced_responses.append(response)
    return unsynced_responses


def is_response_synced(response: dict[str, str]):
    synced_timestamps_data = read_from_files_in_directory(MITM_PROXY_INSTAGRAM_JSON_RESPONSES_SYNCED_LOGS_DIRECTORY_PATH)
    synced_timestamps = synced_timestamps_data.split('\n')

    if 'meta' in response and 'timestamp' in response['meta']:
        return response['meta']['timestamp'] in synced_timestamps

    return True


def sync_responses(responses: list[dict[str, str]]):
    for response in responses:
        sync_response(response)


def sync_response(response: dict[str, str]):
    save_useful_data_from_response_to_database(response)
    save_timestamp_to_synced_txt_file(response['meta']['timestamp'])


def save_useful_data_from_response_to_database(response: dict[str, str]):
    pass


def save_timestamp_to_synced_txt_file(timestamp):
    pass


def run_data_syncs(state: dict):
    while state['data_syncs']['is_running']:
        try:
            sync_instagram_responses_from_files_to_database()
        except:
            pass
        sleep(1)
