from src.utils.utils import build_flat_dict

state = build_flat_dict({
    'program_is_running': True,
    'http_listener': {
        'is_running': False,
        'subprocess_object': None
    },
    'agent': {
        'current_task': None,
        'queue': [],
        'is_running': False,
        'is_subprocess': False,
    },
    'console': {
        'client': {
            'is_running': False,
            'subprocess_object': None
        },
        'server': {
            'is_running': False,
        }
    },
    'mitm_proxy': {
        'is_running': False,
        'subprocess_object': None
    },
    'data_syncs': {
        'is_running': False,
    },
    'content_builder': {
        'is_running': False,
        'subprocess_object': None
    }
})
