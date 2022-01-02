'''EXECUTEABLE PROGRAMS'''
BRAVE_EXECUTEABLE = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
CHROME_EXECUTEABLE = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
CMD_EXECUTEABLE = 'C:/WINDOWS/system32/cmd.exe'

'''MITM OPTIONS'''
MITM_PROXY_FILEPATH = 'src/http_listener/listener'

'''SCRIPTS'''

'''FORMATS'''
TODAY_FORMAT = r'%Y_%m_%d'
TIMESTAMP_FORMAT = r'%H_%M_%S_%f'
DATETIMESTAMP_FORMAT = r'%Y-%m-%d %H:%M:%S.%f'

'''URLS'''
INSTAGRAM_URL = 'https://www.instagram.com'

'''DIRECTORIES'''
BOT_DIRECTORY = 'C:/x/bots'
BOT_FACTORY_PARTS_DIRECTORY = '{}/bot_factory_parts'.format(BOT_DIRECTORY)
INTERACTION_LOGGER_LOGS_DIRECTORY = 'C:/x/logs/interaction-logger'
IG_JSON_RESPONSES_LOGS_DIRECTORY = 'C:/x/logs/mitm-proxy/instagram/json'
IG_JSON_RESPONSES_SYNCED_TIMESTAMP_DIRECTORY = 'C:/x/logs/mitm-proxy-synced/instagram/json'
LISTENER_LOGS_DIRECTORY = 'C:/x/logs/mitm-proxy'
LISTENER_LOGS_SYNCED_DIRECTORY = 'C:/x/logs/mitm-proxy-synced'
LISTENER_LOGS_INSTAGRAM_IMAGES_DIRECTORY = 'C:/x/logs/mitm-proxy/instagram/images'

'''Misc'''
MAX_LOG_FILE_SIZE = 50 * 1000 * 1000