import json
from datetime import datetime, timezone
from types import FunctionType
from flatdict import FlatterDict
from copy import deepcopy
from subprocess import Popen
from src.utils.constants import DATETIMESTAMP_FORMAT, TIMESTAMP_FORMAT, TODAY_FORMAT


def datetime_utc_now():
    return datetime.now(timezone.utc)


def today(datetime_object: datetime=None):
    now = datetime_object if datetime_object else datetime_utc_now()
    return now.strftime(TODAY_FORMAT)


def build_timestamp(datetime_object: datetime=None):
    now = datetime_object if datetime_object else datetime_utc_now()
    return now.strftime(TIMESTAMP_FORMAT)


def build_datetimestamp(datetime_object: datetime=None):
    now = datetime_object if datetime_object else datetime_utc_now()
    return now.strftime(DATETIMESTAMP_FORMAT)


def parse_datetimestamp(datetimestamp: str) -> datetime:
    return datetime.strptime(datetimestamp, DATETIMESTAMP_FORMAT)


def try_parse_json(json_object: str):
    try:
        parsed = json.loads(json_object)
        return parsed
    except:
        print('Could not parse json: {}'.format(json_object))
        return None


def build_flat_dict(nested_dict, delimiter='.'):
    return FlatterDict(nested_dict, delimiter=delimiter)


def get_updated_values(dict1: FlatterDict, dict2: FlatterDict):
    differences = {}

    for key in dict1.keys():
        
        if dict1[key] != dict2[key]:
            differences[key] = dict2[key]
    
    return differences


def copy_state(state: FlatterDict):
    ignore_types = [Popen, FunctionType]

    state_dict = dict(state)
    state_dict_items = state_dict.items()
    state_dict_items_with_ignore_type_object = [(k, v) for (k, v) in state_dict_items if type(v) in ignore_types]
    state_dict_items_without_ignore_type_object = [(k, v) for (k, v) in state_dict_items if type(v) not in ignore_types]

    new_state_dict_items = deepcopy(state_dict_items_without_ignore_type_object)

    new_state_dict_items.extend(state_dict_items_with_ignore_type_object)
    new_state_dict = {}

    for (key, value) in new_state_dict_items:
        new_state_dict[key] = value

    new_state = build_flat_dict(new_state_dict)
    return new_state
    