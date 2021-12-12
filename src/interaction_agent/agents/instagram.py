from src.interaction_agent.agents.browser import open_browser, navigate_to_url, wait_until_browser_loads, toggle_dev_tools, focus_dev_tools
from src.interaction_agent.controls.keyboard import hotkey

def setup():
    open_browser(2)
    navigate_to_url('https://instagram.com')
    toggle_dev_tools()
    focus_dev_tools()
    wait_until_browser_loads()

def exit():
    hotkey(['alt', 'f4'])
