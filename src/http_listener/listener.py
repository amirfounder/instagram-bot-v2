import sys
sys.path.append('C:/Users/Amir Sharapov/Code/amirfounder-automation/x')

from src.http_listener.handle_flow import handle_flow




def request(flow) -> None:
    handle_flow(flow)
