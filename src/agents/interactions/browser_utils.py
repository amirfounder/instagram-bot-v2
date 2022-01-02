from time import sleep
from pyperclip import copy
from src.utils.constants import *
from src.utils.system import move_app_to_monitor, open_app, close_app, get_foreground_app, show_app_maximized
from src.controls.keyboard import hotkey, press_and_release, write


BROWSER_EXECUTEABLE = BRAVE_EXECUTEABLE


def open_browser(monitor: int, maximize: bool):
    open_app(BRAVE_EXECUTEABLE)
    sleep(.5)
    hwnd = get_foreground_app()[0]
    move_app_to_monitor(hwnd, monitor, maximize)

    if maximize:
        show_app_maximized(hwnd)

    return hwnd


def close_browser(hwnd):
    close_app(hwnd)


def navigate_to_url(url: str):
    hotkey(['ctrl', 'l'])
    sleep(.2)
    write(url, .0025)
    sleep(.2)
    press_and_release('enter')
    sleep(.2)


def toggle_dev_tools():
    hotkey(['ctrl', 'shift', 'j'])
    sleep(.2)


def focus_dev_tools():
    hotkey(['ctrl', '`'])
    sleep(.2)


def toggle_dev_tools_docked():
    hotkey(['ctrl', 'shift', 'd'])
    sleep(.2)


def execute_script_in_dev_tools(script: str):
    copy(script)

    if not script.startswith('copy(') or not script.endswith(')'):
        script = 'copy({})'.format(script)

    focus_dev_tools()
    hotkey(['ctrl', 'v'])
    sleep(.2)
    press_and_release('enter')


def wait_until_browser_loads():
    loaded = False

    while (not loaded):
        for _ in range(3):

            script = 'document.readyState'
            result = execute_script_in_dev_tools(script)
            loaded = result == 'complete'

            if loaded:
                break

            sleep(1)

        hotkey(['ctrl', 'r'])


def exit(hwnd):
    close_app(hwnd)
