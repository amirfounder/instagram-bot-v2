from src.agents.interactions.browser_utils import *
from src.controls.keyboard import hotkey, write
from src.data.repository import *
from datetime import datetime

def setup():
    open_browser(2)
    navigate_to_url(INSTAGRAM_URL)
    toggle_dev_tools()
    focus_dev_tools()
    wait_until_browser_loads()


def exit():
    hotkey(['alt', 'f4'])


def research_hashtags(seed_hashtag: str, levels: int):
    start = datetime.now()

    write(seed_hashtag)
    sleep(3)

    hashtags = 0




