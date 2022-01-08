from src.agents.browser import *
from src.agents.controls.keyboard import hotkey, write
from src.data.repository import *


def setup():
    open_browser(2)
    navigate_to_url(INSTAGRAM_URL)


def exit():
    hotkey(['alt', 'f4'])


def research_hashtags(seed_hashtag: str, levels: int):
    start = None

    write(seed_hashtag)
    sleep(3)

    hashtags = 0
