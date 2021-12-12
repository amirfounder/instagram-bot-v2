from random import Random
from time import sleep
import mouse


random = Random()


def get_current_position():
    return mouse.get_position()


def move_to_box(box, duration=.2, spacing=5):
	x, y, width, height = [int(x) for x in box]

	x_lower = x + spacing
	x_upper = x + width - spacing
	y_lower = y + spacing
	y_upper = y + height - spacing

	rx = random.randint(x_lower, x_upper)
	ry = random.randint(y_lower, y_upper)

	move_to((rx, ry), duration=duration)


def move_to(coords, duration=.2):
    x, y = coords
    mouse.move(x, y, absolute=True, duration=duration)


def move(coords, duration=.2):
    x, y = coords
    mouse.move(x, y, absolute=False, duration=duration)


def click(control="left", duration=.08):
    press(control)
    sleep(duration)
    release(control)


def press(control='left'):
    mouse.press(control)


def release(control='left'):
    mouse.release(control)
