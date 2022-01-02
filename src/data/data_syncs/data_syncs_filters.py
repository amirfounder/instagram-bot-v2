from src.data.data_syncs.data_syncs_utils import get_datetimes_of_synced_responses
from src.utils.string_literals import X_METADATA, DATETIMESTAMP


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


def filter_useless_responses(responses: list[dict]) -> list[dict]:
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


def filter_responses_with_no_datetime(unfiltered_responses: list[dict]):
    return [x for x in unfiltered_responses if X_METADATA in x and DATETIMESTAMP in x[X_METADATA]]


def filter_synced_responses(responses: list[dict]):
    datetimes_of_synced_responses = get_datetimes_of_synced_responses()
    unsynced_responses = []

    for response in responses:
        if response[X_METADATA][DATETIMESTAMP] not in datetimes_of_synced_responses:
            unsynced_responses.append(response)
    
    return unsynced_responses
