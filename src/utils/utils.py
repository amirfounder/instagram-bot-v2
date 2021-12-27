import json
from datetime import datetime
from flatdict import FlatDict, FlatterDict
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
    differences = list(differences)
    return differences