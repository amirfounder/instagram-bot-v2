
def handle_instagram_response(flow):
  pass

def is_json(flow):
  pass

def is_image(flow):
  pass

def content_type_is_json(flow):
    for key, value in flow.response.headers.items():
      if key == 'content-type':
        return 'application/json' in value
    return False

def content_type_is_image(flow):
    for key, value in flow.response.headers.items():
      if key == 'content-type':
        return 'image' in value
    return False

