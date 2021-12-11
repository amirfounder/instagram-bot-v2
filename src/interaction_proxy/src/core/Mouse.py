from random import Random
import mouse
import time


class Mouse:
  def __init__(self) -> None:
    self.pressed = []
    self._rand = Random()

  def current(self):
    return mouse.get_position()

  def move_to_box(self, box, duration=.2, spacing=5):
    left, top, width, height = [int(x) for x in box]
    x = self._rand.randint(left, left + width)
    y = self._rand.randint(top, top + height)
    self.move_to((x, y), duration=duration)

  def move_to(self, coords, duration=.2):
    x, y = coords
    mouse.move(x, y, absolute=True, duration=duration)

  def move(self, coords, duration=.2):
    x, y = coords
    mouse.move(x, y, absolute=False, duration=duration)

  def scroll(self, direction, duration=0):
    if direction in ['down', -1]:
      time.sleep(duration)
      mouse.wheel(-1)
    elif direction in ['up', 1]:
      time.sleep(duration)
      mouse.wheel(1)

  def click(self, control="left", duration=.08):
    self.press(control)
    time.sleep(duration)
    self.release(control)

  def press(self, control='left'):
    mouse.press(control)

  def release(self, control='left'):
    mouse.release(control)

  def is_pressed(self, control):
    return control in self.pressed