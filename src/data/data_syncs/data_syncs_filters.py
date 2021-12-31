from src.data.data_syncs.data_syncs_utils import get_synced_responses_timestamps


keys_of_responses_with_no_value = [
    [
        'checksum',
        'config',
        'config_owner_id',
        'app_data',
        'qpl_version',
        'x-metadata'
    ],
    ['status', 'x-metadata', 'fr'],
    ['status', 'x-metadata']
]


def filter_useless_responses(responses: list[dict]):
    filter_criteria = keys_of_responses_with_no_value
    for criteria in filter_criteria:
        criteria.sort()

    filtered_responses = []

    for response in responses:
        response_keys = list(response.keys())
        response_keys.sort()
        if response_keys not in filter_criteria:
            filtered_responses.append(response)

    return filtered_responses


def filter_responses_with_no_timestamp(unfiltered_responses: list[dict]):
    return [x for x in unfiltered_responses if 'x-metadata' in x and 'timestamp' in x['x-metadata']]


def filter_synced_responses(responses: list[dict]):
    synced_responses_timestamps = get_synced_responses_timestamps()

    unsynced_responses = []
    for response in responses:
        if response['x-metadata']['timestamp'] not in synced_responses_timestamps:
            unsynced_responses.append(response)
    return unsynced_responses
