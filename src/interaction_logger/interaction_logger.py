from datetime import datetime
from typing import Any
from pynput import mouse, keyboard
from threading import Thread
from src.data_manager.files import create_directories, append_to_file_in_directory
from src.utils.constants import INTERACTION_LOGGER_LOGS_DIRECTORY_PATH


class MyException(Exception):
    pass


VERSION = 1

KILL_KEY_ONE = keyboard.Key.shift_r
KILL_KEY_TWO = keyboard.Key.ctrl_r

MOUSE_PRESS_EVENT = 'mp'
MOUSE_RELEASE_EVENT = 'mr'
MOUSE_MOVE_EVENT = 'mm'
MOUSE_SCROLL_EVENT = 'ms'
KEY_PRESS_EVENT = 'kp'
KEY_RELEASE_EVENT = 'kr'

kill_key_one_pressed = False
kill_key_two_pressed = False
kill_logger = False


def run():
    create_directories(INTERACTION_LOGGER_LOGS_DIRECTORY_PATH)

    thread_one = Thread(target=run)
    thread_two = Thread(target=run)
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()


def run_keyboard_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except MyException:
            print('stopping')


def run_mouse_listener():
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll, on_move=on_move) as listener:
        try:
            listener.join()
        except MyException:
            print('stopping')


def on_click(x, y, button, pressed):
    e_type = MOUSE_PRESS_EVENT if pressed else MOUSE_RELEASE_EVENT
    e_button = 'l' if button == mouse.Button.left else 'r'
    e = '{},{},{},{}'.format(e_type, x, y, e_button)
    log(e)
    try_kill_logger()


def on_move(x, y):
    e = '{},{},{}'.format(MOUSE_MOVE_EVENT, x, y)
    log(e)
    try_kill_logger()


def on_scroll(x, y, dx, dy):
    e = '{},{},{},{},{}'.format(MOUSE_SCROLL_EVENT, x, y, dx, dy)
    log(e)
    try_kill_logger()


def on_press(key):
    e = '{},{}'.format(KEY_PRESS_EVENT, key)
    log(e)
    handle_potential_kill_key(KEY_PRESS_EVENT, key)
    try_kill_logger()

	
def on_release(key):
    e = '{}{}'.format(KEY_RELEASE_EVENT, key)
    log(e)
    handle_potential_kill_key(KEY_RELEASE_EVENT, key)
    try_kill_logger()


def log(event: str):
    now = datetime.now()

    timestamp = 't'.format(now.strftime(r'%H_%M_%S_%f'))
    version = 'v{}'.format(VERSION)
    content = '{}{}{}'.format(version, timestamp, event)

    today = now.strftime(r'%Y_%m_%d')
    directory = '{}/{}'.format(INTERACTION_LOGGER_LOGS_DIRECTORY_PATH, today)

    append_to_file_in_directory(directory, content)


def try_kill_logger():
    if kill_logger:
        raise MyException()


def handle_potential_kill_key(event_type: str, key: Any):
	if event_type == KEY_PRESS_EVENT:
		if key == KILL_KEY_ONE:
			kill_key_one_pressed = True
		if key == KILL_KEY_TWO:
			kill_key_two_pressed = True

	if event_type == KEY_RELEASE_EVENT:
		if key == KILL_KEY_ONE:
			kill_key_one_pressed = False
		if key == KILL_KEY_TWO:
			kill_key_two_pressed = False
	
	if kill_key_one_pressed and kill_key_two_pressed:
		kill_logger = True
	
	if kill_logger:
		raise MyException()
