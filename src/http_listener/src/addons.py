from src.data_manager import FileManager
from datetime import datetime
from src.http_listener.src.handle_flow import *


class HttpListener:

    def __init__(self) -> None:
        now = datetime.now()
        target_directory = 'C:/x/logs/mitm-proxy/' + now.strftime('%Y_%m_%d')
        self.file_manager = FileManager(target_directory=target_directory)

    def request(self, flow) -> None:
        if is_from_instagram(flow):
            handle_instagram_response(flow)

    def done(self):
        print("Done.")
