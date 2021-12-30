import json
from datetime import datetime
from flatdict import FlatterDict
from copy import copy, deepcopy
from subprocess import Popen
from src.utils.constants import TIMESTAMP_FORMAT, TODAY_FORMAT



def today(now: datetime=None):
    now = now if now else datetime.now()
    return now.strftime(TODAY_FORMAT)


def timestamp(now: datetime=None):
    now = now if now else datetime.now()
    return now.strftime(TIMESTAMP_FORMAT)


def try_parse_json(json_object: str):
    try:
        parsed = json.loads(json_object)
        return parsed
    except:
        print('Could not parse json: {}'.format(json_object))
        return None


def build_flat_dict(nested_dict, delimiter='.'):
    return FlatterDict(nested_dict, delimiter=delimiter)


def get_differences_from_prev_state(prev_state: FlatterDict, current_state: FlatterDict):
    differences = {}

    for key in prev_state.keys():
        
        if prev_state[key] != current_state[key]:
            differences[key] = current_state[key]
    
    return differences


def copy_state(initial_state: FlatterDict):
    initial_state_dict = dict(initial_state)

    initial_state_dict_items = initial_state_dict.items()
    initial_state_dict_items_with_popen_object = [(k, v) for (k, v) in initial_state_dict_items if type(v) is Popen]
    initial_state_dict_items_without_popen_object = [(k, v) for (k, v) in initial_state_dict_items if type(v) is not Popen]

    new_state_dict_items = deepcopy(initial_state_dict_items_without_popen_object)
    new_state_dict_items.extend(initial_state_dict_items_with_popen_object)

    new_state_dict = {}

    for (key, value) in new_state_dict_items:
        new_state_dict[key] = value

    new_state = build_flat_dict(new_state_dict)
    return new_state
    