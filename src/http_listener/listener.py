import sys
sys.path.append('C:/Users/Amir Sharapov/Code/amirfounder-automation/x')

from src.http_listener.handle_http_flow import handle_http_flow


def response(flow) -> None:
    handle_http_flow(flow)


def running() -> None:
    pass

