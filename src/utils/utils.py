import json
from datetime import datetime
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


def recusrively_get_keys_from_dict(dict_object: dict):
    keys = list(dict_object.keys())
    for key in keys:
        if type(dict_object[key]) == dict:
            local_keys = recusrively_get_keys_from_dict(dict_object[key])
            keys.extend(local_keys)
    return keys
