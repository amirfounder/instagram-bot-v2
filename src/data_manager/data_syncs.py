from time import sleep

from src.data_manager.database import save_all, update_all
from src.data_manager.repository import get_instagram_users_by_attr
from src.data_manager.data_syncs_utils import parse_json_responses
from src.data_manager.data_syncs_filters import \
    filter_useless_responses, \
        filter_responses_with_no_timestamp, \
            filter_synced_responses
from src.data_manager.data_syncs_entity_builders import build_instagram_user_to_save, build_instagram_user_to_update
from src.data_manager.files import append_to_file_in_directory, convert_data_map_to_data, read_from_files_in_directory
from src.utils.constants import IG_JSON_RESPONSES_LOGS_DIRECTORY, IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY


def sync_databases(state: dict):
    print('lol')
    while state['program_is_running']:
        if state['data_syncs.is_running']:
            try:
                sync_instagram_responses_from_files_to_database()
                print('synced')
            except Exception as e:
                print(e)
        sleep(2)


def sync_instagram_responses_from_files_to_database():
    data_map = read_from_files_in_directory(IG_JSON_RESPONSES_LOGS_DIRECTORY)
    data = convert_data_map_to_data(data_map)

    json_responses = data.split('\n')
    json_responses = [x for x in json_responses if x != '']

    responses = parse_json_responses(json_responses)

    responses = filter_responses_with_no_timestamp(responses)
    responses = filter_useless_responses(responses)
    responses = filter_synced_responses(responses)

    sync_responses(responses)


def sync_responses(responses: list[dict]):
    for response in responses:
        save_useful_data_from_response_to_database(response)
        save_timestamp_to_synced_txt_file(response['x-metadata']['timestamp'])


def save_useful_data_from_response_to_database(response: dict):
    if response_contains_account_recommendations(response):
        save_account_recommendations(response)
    if response_contains_hashtag_information(response):
        pass
    if response_contains_posts_information(response):
        pass


def save_account_recommendations(response: dict):
    response_timestamp = response['x-metadata']['timestamp']
    
    json_users = response['users']
    json_users_ig_ids = [int(x['pk']) for x in json_users]

    db_users = get_instagram_users_by_attr('ig_id', json_users_ig_ids)
    db_users = [x for x in db_users if x.timestamp_logged != response_timestamp]
    
    db_users_ig_ids = [int(x.ig_id) for x in db_users]

    users_to_save = []
    users_to_update = []

    for json_user in json_users:
        json_user_ig_id = json_user['pk']

        if json_user_ig_id in db_users_ig_ids:
            db_user = [x for x in db_users if x.ig_id == json_user_ig_id][0]
            user = build_instagram_user_to_update(db_user, json_user, response_timestamp)
            users_to_update.append(user)

        else:
            user = build_instagram_user_to_save(json_user, response_timestamp)
            users_to_save.append(user)

    save_all(users_to_save)
    update_all(users_to_update)


def response_contains_posts_information(response: dict):
    pass


def response_contains_hashtag_information(response: dict):
    pass


def response_contains_account_recommendations(response: dict):
    url = response['x-metadata']['url']
    identifier = 'accounts_recs'

    return identifier in url


def save_timestamp_to_synced_txt_file(timestamp: str):
    append_to_file_in_directory(
        IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY, timestamp)
