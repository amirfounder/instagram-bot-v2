import keyboard
import time


def write(value: str, delay=.05):
    for i in range(len(value)):
        char = value[i]
        keyboard.write(char, delay=delay)


def press_and_release(value, interval=0.03):
    press(value)
    time.sleep(interval)
    release(value)


def press(value):
    keyboard.press(value)


def release(value):
    keyboard.release(value)


def backspace(count=1):
    for _ in range(count):
        press_and_release('backspace')


def hotkey(keys: list, interval: int = .03):
    keys_reverse = keys.copy()
    keys_reverse.reverse()

    for key in keys:
        press(key)
        time.sleep(interval)

    for key in keys_reverse:
        release(key)
        time.sleep(interval)
