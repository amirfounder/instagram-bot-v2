from src.http_listener import InstagramResponseHandler
from src.data_manager import FileManager
from datetime import datetime

class HttpProxy:
  
  def __init__(self) -> None:
    now = datetime.now()
    target_directory = 'C:/x/logs/mitm-proxy/' + now.strftime('%Y_%m_%d')
    self.file_manager = FileManager(target_directory=target_directory)
    self.__instagram_response_handler = InstagramResponseHandler()

  def response(self, flow) -> None:
    if "instagram" in flow.request.pretty_url:
      self.__instagram_response_handler.handle_response(flow)
  
