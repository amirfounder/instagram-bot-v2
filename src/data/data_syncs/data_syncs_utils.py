from src.data.files import read_from_files_in_directory, convert_data_map_to_data
from src.utils.constants import IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY
from src.utils.utils import try_parse_json


def get_synced_responses_timestamps():
    synced_timestamps_data_map = read_from_files_in_directory(
        IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY)
    synced_timestamps_data = convert_data_map_to_data(
        synced_timestamps_data_map)
    synced_timestamps = synced_timestamps_data.split('\n')

    return synced_timestamps


def parse_json_responses(json_responses: list[str]):
    parsed_responses = []

    for json_response in json_responses:
        parsed_response = try_parse_json(json_response)
        if parsed_response is not None:
            parsed_responses.append(parsed_response)

    return parsed_responses