from time import sleep, time
from src.data_manager.database import build_session, save_all, update_all
from src.data_manager.database_entities import InstagramHashtag, InstagramPost, InstagramUser
from src.data_manager.files import append_to_file_in_directory, convert_data_map_to_data, read_from_files_in_directory
from src.utils.constants import IG_JSON_RESPONSES_LOGS_DIRECTORY, IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY
from src.utils.utils import try_parse_json


def run_data_syncs(state: dict):
    while state['data_syncs']['is_running']:
        try: sync_instagram_responses_from_files_to_database()
        except: pass
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
        save_account_recommendations(response)
    if response_contains_hashtag_information(response):
        pass
    if response_contains_posts_information(response):
        pass



def save_account_recommendations(response: dict):
    response_timestamp = response['x-metadata']['timestamp']
    users_from_response = response['users']
    users_from_response_ig_ids = [int(x['pk']) for x in users_from_response]

    session = build_session()
    query = session \
        .query(InstagramUser) \
        .filter(InstagramUser.ig_id.in_(users_from_response_ig_ids))

    existing_users = query.all()
    existing_users_ig_ids = [int(x.ig_id) for x in existing_users]

    users_to_save = []
    users_to_update = []

    for user_from_response in users_from_response:
        user_from_response_ig_id = user_from_response['pk']

        if user_from_response_ig_id in existing_users_ig_ids:
            existing_user = [x for x in existing_users if x.ig_id == user_from_response_ig_id][0]
            
            if existing_user.timestamp_logged == response_timestamp:
                continue

            user = build_instagram_user_to_update(existing_user, user_from_response, response_timestamp)
            users_to_update.append(user)

        else:
            user = build_instagram_user_to_save(user_from_response, response_timestamp)
            users_to_save.append(user)

    save_all(users_to_save)
    update_all(users_to_update)


def build_instagram_user_to_save(user_as_dict: dict, timestamp: str):
    user = InstagramUser()
    user.ig_id = user_as_dict['pk']
    user.username = user_as_dict['username']
    user.full_name = user_as_dict['full_name']
    user.private = user_as_dict['is_private']
    user.verified = user_as_dict['is_verified']
    user.timestamp_logged = timestamp
    user.timestamp_updated = timestamp
    return user


def build_instagram_user_to_update(user: InstagramUser, user_as_dict: dict, timestamp: str):
    user.timestamp_updated = timestamp
    return user


def build_instagram_post_to_update(post: InstagramPost, post_as_dict: dict, timestamp: str):
    pass


def build_instagram_post_to_save(post_as_dict: dict, timestamp: str):
    pass


def build_instagram_hashtag_to_save(hashtag_as_dict: dict, timestamp: str):
    pass


def build_instagram_hashtag_to_update(hashtag: InstagramHashtag, hashtag_as_dict: dict, timestamp: str):
    pass


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
