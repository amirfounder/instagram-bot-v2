import keyboard
import time


class Keyboard:

  def __init__(self) -> None:
    self.pressed = []

  def write(self, value:str, delay=.05):
    for i in range(len(value)):
      char = value[i]
      keyboard.write(char, delay=delay)

  def press_and_release(self, value, interval=0.03):
    self.press(value)
    time.sleep(interval)
    self.release(value)

  def press(self, value):
    keyboard.press(value)
    self.pressed.append(value)

  def release(self, value):
    keyboard.release(value)
    self.pressed.remove(value)
  
  def backspace(self, count=1):
    for _ in range(count):
      self.press_and_release('backspace')

  def is_pressed(self, value):
    return value in self.pressed
