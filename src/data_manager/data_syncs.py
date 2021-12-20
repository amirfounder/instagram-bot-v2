from time import sleep
from src.data_manager.database import save_all
from src.data_manager.database_entities import InstagramUser
from src.data_manager.files import append_to_file_in_directory, convert_data_map_to_data, read_from_files_in_directory
from src.utils.constants import IG_JSON_RESPONSES_LOGS_DIRECTORY, IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY
from src.utils.utils import try_parse_json


def run_data_syncs(state: dict):
    while state['data_syncs']['is_running']:
        try:
            sync_instagram_responses_from_files_to_database()
        except Exception as e:
            print(e)
            pass
        sleep(2)


def sync_instagram_responses_from_files_to_database():
    data_map = read_from_files_in_directory(IG_JSON_RESPONSES_LOGS_DIRECTORY)
    data = convert_data_map_to_data(data_map)

    json_responses = data.split('\n')
    json_responses = [x for x in json_responses if x != '']
    parsed_responses = parse_list_json_responses(json_responses)

    filtered_responses = filter_responses_with_no_timestamp_record(
        parsed_responses)
    filtered_responses = filter_responses_with_no_value(filtered_responses)

    unsynced_responses = get_unsynced_responses(filtered_responses)

    sync_responses(unsynced_responses)


def parse_list_json_responses(json_responses: list[str]):
    parsed_responses = []

    for json_response in json_responses:
        parsed_response = try_parse_json(json_response)
        if parsed_response is not None:
            parsed_responses.append(parsed_response)

    return parsed_responses


def filter_responses_with_no_timestamp_record(unfiltered_responses: list[dict]):
    return [x for x in unfiltered_responses if 'x-metadata' in x and 'timestamp' in x['x-metadata']]


def filter_responses_with_no_value(responses: list[dict]):
    filter_criteria = [
        ['checksum', 'config', 'config_owner_id',
            'app_data', 'qpl_version', 'x-metadata'],
        ['status', 'x-metadata', 'fr'],
        ['status', 'x-metadata']
    ]
    for criteria in filter_criteria:
        criteria.sort()

    filtered_responses = []

    for response in responses:
        response_keys = list(response.keys())
        response_keys.sort()
        if response_keys not in filter_criteria:
            filtered_responses.append(response)

    return filtered_responses


def get_unsynced_responses(responses: list[dict]):
    synced_responses_timestamps = get_synced_responses_timestamps()

    unsynced_responses = []
    for response in responses:
        if response['x-metadata']['timestamp'] not in synced_responses_timestamps:
            unsynced_responses.append(response)
    return unsynced_responses


def get_synced_responses_timestamps():
    synced_timestamps_data_map = read_from_files_in_directory(
        IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY)
    synced_timestamps_data = convert_data_map_to_data(
        synced_timestamps_data_map)
    synced_timestamps = synced_timestamps_data.split('\n')

    return synced_timestamps


def sync_responses(responses: list[dict]):
    for response in responses:
        sync_response(response)


def sync_response(response: dict):
    save_useful_data_from_response_to_database(response)
    save_timestamp_to_synced_txt_file(response['x-metadata']['timestamp'])


def save_useful_data_from_response_to_database(response: dict):
    if response_contains_account_recommendations(response):
        users = response['users']
        users_to_save = []

        for user in users:

            user_to_save = InstagramUser()
            user_to_save.ig_id = user['pk']
            user_to_save.username = user['username']
            user_to_save.full_name = user['full_name']
            user_to_save.private = user['is_private']
            user_to_save.verified = user['is_verified']
            users_to_save.append(user_to_save)

        for user_to_save in users_to_save:
            pass


def response_contains_account_recommendations(response: dict):
    url = response['x-metadata']['url']
    identifier = 'accounts_recs'

    return identifier in url


def save_timestamp_to_synced_txt_file(timestamp: str):
    append_to_file_in_directory(
        IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY, timestamp)
