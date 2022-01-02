from time import sleep

from src.data.repository import save_all_instagram_users, get_all_instagram_users_by_attr
from src.data.data_syncs.data_syncs_utils import parse_json_responses
from src.data.data_syncs.data_syncs_filters import *
from src.data.data_syncs.data_syncs_entity_builders import build_instagram_user_to_save, build_instagram_user_to_update
from src.data.database.entities import InstagramUser
from src.data.files import append_to_file_in_directory, convert_data_map_to_data, read_from_files_in_directory
from src.utils.constants import IG_JSON_RESPONSES_LOGS_DIRECTORY, IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY
from src.utils.string_literals import DATETIMESTAMP, URL


def sync_databases(state: dict):
    while state['program_is_running']:
        if state['data_syncs.is_running']:
            try:
                sync_instagram_responses_from_files_to_database()
            except Exception as e:
                print(e)
        sleep(3)


def sync_instagram_responses_from_files_to_database():
    data_map = read_from_files_in_directory(IG_JSON_RESPONSES_LOGS_DIRECTORY)
    data = convert_data_map_to_data(data_map)

    json_responses = data.split('\n')
    json_responses = [x for x in json_responses if x != '']
    responses = parse_json_responses(json_responses)

    responses = filter_responses_with_no_datetime(responses)
    responses = filter_useless_responses(responses)
    responses = filter_synced_responses(responses)

    sync_responses(responses)


def sync_responses(responses: list[dict]):

    for response in responses:
        save_response_data_to_database(response)
        save_datetime_to_synced_txt_file(response[X_METADATA][DATETIMESTAMP])


def save_response_data_to_database(response: dict):
    if response_contains_account_recommendations(response):
        save_account_recommendations(response)

    if response_contains_hashtag_information(response):
        save_hashtag_information(response)

    if response_contains_posts_information(response):
        save_posts_information(response)


def save_hashtag_information(response: dict):
    pass


def save_posts_information(response: dict):
    pass


def save_account_recommendations(response: dict):
    json_users = response['users']
    json_users_platform_ids = [int(x['pk']) for x in json_users]

    response_timestamp = response[X_METADATA][DATETIMESTAMP]

    db_users: list[InstagramUser]
    db_users = get_all_instagram_users_by_attr('platform_id', json_users_platform_ids)
    db_users = [x for x in db_users if x.datetime_of_initial_log != response_timestamp]
    db_users_platform_ids = [int(x.platform_id) for x in db_users]

    users_to_save = []
    users_to_update = []

    for json_user in json_users:
        json_user_platform_id = json_user['pk']

        if json_user_platform_id in db_users_platform_ids:
            db_user = [x for x in db_users if x.platform_id == json_user_platform_id][0]
            user = build_instagram_user_to_update(db_user, json_user, response_timestamp)
            users_to_update.append(user)

        else:
            user = build_instagram_user_to_save(json_user, response_timestamp)
            users_to_save.append(user)

    save_all_instagram_users(users_to_save)


def response_contains_posts_information(response: dict):
    pass


def response_contains_hashtag_information(response: dict):
    pass


def response_contains_account_recommendations(response: dict):
    url = response[X_METADATA][URL]
    identifier = 'accounts_recs'

    return identifier in url


def save_datetime_to_synced_txt_file(datetime: str):
    append_to_file_in_directory(
        IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY, datetime)
