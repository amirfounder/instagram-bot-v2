from src.utils.utils import build_flat_dict

state = build_flat_dict({
    'program_is_running': True,
    'instagram_agent': {
        'current_task': None,
        'tasks': {
            'research_hashtags': {
                'is_running': False,
                'seed_hashtag': None,
                'network_depth': 2
            },
            'explore_recommended_accounts': {
                'is_running': False,
                'seed_account': False,
                'network_depth': 2
            },
            'identify_popular_posts': {
                'is_running': False,
                'account_username': None
            },
            'engage_on_platform': {
                'is_running': False,
            }
        },
        'is_running': False,
        'is_subprocess': False,
    },
    'console': {
        'client': {
            'is_running': False,
            'is_subprocess': True,
            'subprocess_object': None
        },
        'server': {
            'is_running': False,
            'is_subprocess': False
        }
    },
    'mitm_proxy': {
        'is_running': False,
        'is_subprocess': True,
        'subprocess_object': None
    },
    'data_syncs': {
        'is_running': False,
        'is_subprocess': False
    },
    'database_setup': {
        'completed': False
    },
    'content_builder': {
        'is_running': False,
        'is_subprocess': True,
        'subprocess_object': None
    }
})