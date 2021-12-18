import importlib
import sys
import time
sys.path.append('C:/Users/Amir Sharapov/Code/amirfounder-automation/x')

from src.http_listener.handle_flow import handle_flow
import src.config as config


def request(flow) -> None:
    handle_flow(flow)


def running() -> None:
    pass

