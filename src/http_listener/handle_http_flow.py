from mitmproxy.http import HTTPFlow
from datetime import datetime
from json import loads, dumps
from src.data.files import append_to_file_in_directory, save_bytes_to_image_in_directory
from src.utils.constants import IG_JSON_RESPONSES_LOGS_DIRECTORY
from src.utils.utils import timestamp


def handle_http_flow(flow: HTTPFlow):
    if is_from_instagram(flow):
        handle_instagram_response(flow)


def is_from_instagram(flow: HTTPFlow):
    return 'instagram' in flow.request.pretty_url


def handle_instagram_response(flow: HTTPFlow):
    print('Handling instagram flow: {}'.format(flow.request.pretty_url))

    if is_json(flow):
        save_json(flow)
    if is_image(flow):
        save_image(flow)

    print('Handled instagram flow: {}'.format(flow.request.pretty_url))


def is_json(flow: HTTPFlow):
    return 'application/json' in get_content_type(flow)


def is_image(flow: HTTPFlow):
    return 'image' in get_content_type(flow)


def get_content_type(flow: HTTPFlow) -> str:
    return get_header(flow, 'content-type')


def get_header(flow: HTTPFlow, key: str) -> str:
    return flow.response.headers.get(key, '')


def save_image(flow: HTTPFlow):
    directory = 'C:/x/logs/mitm-proxy/instagram/images'
    data = flow.response.content
    ts = timestamp()

    save_bytes_to_image_in_directory(directory, data, ts)


def save_json(flow: HTTPFlow):
    data = flow.response.text
    directory = IG_JSON_RESPONSES_LOGS_DIRECTORY
    loaded = None

    try:
        loaded = loads(data)
        metadata = build_metadata(flow)
        loaded['x-metadata'] = metadata
        data = dumps(loaded)
    except:
        pass

    data = '{}\n'.format(data)
    append_to_file_in_directory(directory, data)


def build_metadata(flow: HTTPFlow):
    return {
          'url': flow.request.pretty_url,
          'timestamp': datetime.now().strftime('%Y%m%d_%H%M%S.%f')
    }


def content_type_is_json(flow: HTTPFlow):
    for key, value in flow.response.headers.items():
        if key == 'content-type':
            return 'application/json' in value
    return False
