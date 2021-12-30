import json
from datetime import datetime
from flatdict import FlatDict, FlatterDict
from copy import copy
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


def find_differences_between_two_flat_dicts(dict1: FlatterDict, dict2: FlatterDict):
    dict1_set = set(dict1.items())
    dict2_set = set(dict2.items())

    differences = dict1_set ^ dict2_set
    differences = dict(differences)

    return differences


def copy_state():
    new_state = {}
    

def deep_copy_dictionary(initial_dict: dict, ignore_value_types: list[type] = []):
    new_dict = {}

    for key, value in initial_dict.items():
        
        value_type = type(value)

        if value_type in ignore_value_types:
            new_dict[key] = value
        
        elif value_type is dict:
            new_value = deep_copy_dictionary(value, ignore_value_types)
            new_dict[key] = new_value
        
        elif value_type is list:
            new_value = deep_copy_list(value)
            new_dict[key] = new_value
        
        else:
            new_value = copy(value)
            new_dict[key] = new_value
    
    return new_dict


def deep_copy_list(initial_list: list):
    new_list = []

    for item in initial_list:
        
        if type(item) is dict:
            new_item = deep_copy_dictionary(item)
            new_list.append(new_item)
        
        elif type(item) is list:
            new_item = deep_copy_list(item)
            new_list.append(new_item)
        
        else:
            new_item = copy(item)
            new_list.append(new_item)
    
    return new_list