class FlowUtils():
  @staticmethod
  def content_type_is_json(flow):
    for key, value in flow.response.headers.items():
      if key == 'content-type':
        return 'application/json' in value
    return False

  @staticmethod
  def content_type_is_image(flow):
    for key, value in flow.response.headers.items():
      if key == 'content-type':
        return 'image' in value
    return False