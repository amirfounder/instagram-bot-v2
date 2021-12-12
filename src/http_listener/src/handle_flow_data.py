"""TODO
"""
import json
from mitmproxy.http import HTTPFlow
from datetime import datetime
from src.data_manager.src.handle_files import save_image_to_file, append_to_file_in_directory


def save_image(flow: HTTPFlow):
	directory = 'C:/x/logs/mitm-proxy/instagram/images'
	data = flow.response.content

	save_image_to_file(directory, data)


def save_json(flow: HTTPFlow):
	data = flow.response.text
	directory = None
	loaded = None

	try:
		loaded = json.loads(data)
	except:
		pass

	loaded['meta'] = build_meta(flow)
	new_data = json.dumps(loaded)

	append_to_file_in_directory(directory, new_data)



def build_meta(flow: HTTPFlow):
	return {
      	'url': flow.request.pretty_url,
      	'timestamp': datetime.now().strftime('%Y%m%d_%H%M%S.%f')
    }