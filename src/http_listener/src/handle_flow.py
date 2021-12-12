from mitmproxy.http import HTTPFlow


def is_from_instagram(flow: HTTPFlow):
    return 'instagram' in flow.request.pretty_url


def handle_instagram_response(flow: HTTPFlow):
    pass


def is_json(flow: HTTPFlow):
    return 'application/json' in get_content_type(flow)


def is_image(flow: HTTPFlow):
    return 'image' in get_content_type(flow)


def get_content_type(flow: HTTPFlow) -> str:
    return get_header(flow, 'content-type')


def get_header(flow: HTTPFlow, key: str) -> str:
    return flow.response.headers.get(key, '')


def content_type_is_json(flow: HTTPFlow):
    for key, value in flow.response.headers.items():
        if key == 'content-type':
            return 'application/json' in value
    return False
