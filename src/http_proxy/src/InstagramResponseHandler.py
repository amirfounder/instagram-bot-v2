from datetime import datetime
from typing import cast
from src.data_manager import FileManager
from src.http_proxy.src.FlowUtils import FlowUtils
import json


class InstagramResponseHandler():
  def __init__(self):
    self.__image_file_manager = FileManager()
    self.__response_file_manager = FileManager(target_directory='C:/x/logs/mitm-proxy/instagram/json')
    self.__prev_response_id = 0

  def handle_response(self, flow):
    print(f"instagram response : {flow.request.pretty_url}")

    if FlowUtils.content_type_is_json(flow):
      self.handle_json(flow)
    
    if FlowUtils.content_type_is_image(flow):
      self.handle_image(flow)

  def handle_json(self, flow):
    data = flow.response.text

    try:
      data = json.loads(data)
    except:
      return

    data['meta'] = self.build_meta(flow)
    data = json.dumps(data)

    self.__response_file_manager.write_to_directory(str(data))
    self.__prev_response_id += 1

  def build_meta(self, flow):
    return {
      'id': self.__prev_response_id + 1,
      'url': flow.request.pretty_url
    }
    
  def handle_image(self, flow):
    data = flow.response.content
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S.%f')
    images_directory = 'C:/x/logs/mitm-proxy/instagram/images'
    self.__image_file_manager.write_bytearray_to_file(data, f'{images_directory}/{timestamp}.png')