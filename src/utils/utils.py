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
