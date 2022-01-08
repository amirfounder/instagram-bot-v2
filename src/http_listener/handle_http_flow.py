from json import loads, dumps
from mitmproxy.http import HTTPFlow
from src.data.files import append_to_file_in_directory, save_bytes_to_image_in_directory
from src.utils.constants import IG_JSON_RESPONSES_LOGS_DIRECTORY, LISTENER_LOGS_INSTAGRAM_IMAGES_DIRECTORY
from src.utils.string_literals import *
from src.utils.utils import build_datetimestamp, build_timestamp


def handle_http_flow(flow: HTTPFlow):
    if is_from_instagram(flow):
        handle_instagram_response(flow)


def is_from_instagram(flow: HTTPFlow):
    return INSTAGRAM in flow.request.pretty_url


def handle_instagram_response(flow: HTTPFlow):
    print('Handling instagram flow: {}...'.format(flow.request.pretty_url))

    if is_json(flow):
        save_json(flow)
    if is_image(flow):
        save_image(flow)

    print('Handled instagram flow: {}!'.format(flow.request.pretty_url))


def is_json(flow: HTTPFlow):
    return APPLICATION_JSON in get_content_type(flow)


def is_image(flow: HTTPFlow):
    return IMAGE in get_content_type(flow)


def get_content_type(flow: HTTPFlow) -> str:
    return get_header(flow, CONTENT_TYPE)


def get_header(flow: HTTPFlow, key: str) -> str:
    return flow.response.headers.get(key, '')


def save_image(flow: HTTPFlow):
    directory = LISTENER_LOGS_INSTAGRAM_IMAGES_DIRECTORY
    data = flow.response.content
    timestamp = build_timestamp()

    save_bytes_to_image_in_directory(directory, data, timestamp)


def save_json(flow: HTTPFlow):
    data = flow.response.text
    directory = IG_JSON_RESPONSES_LOGS_DIRECTORY
    loaded = None

    try:
        loaded = loads(data)
        metadata = build_metadata(flow)
        loaded[X_METADATA] = metadata
        data = dumps(loaded)
    except:
        pass

    data = '{}\n'.format(data)
    append_to_file_in_directory(directory, data)


def build_metadata(flow: HTTPFlow):
    return {
        URL: flow.request.pretty_url,
        DATETIMESTAMP: build_datetimestamp(),
        VERSION: '1'
    }


def content_type_is_json(flow: HTTPFlow):
    for key, value in flow.response.headers.items():
        if key == CONTENT_TYPE:
            return APPLICATION_JSON in value
    return False
