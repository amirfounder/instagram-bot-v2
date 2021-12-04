from src.interaction_proxy.src.core import Keyboard, Screen, Mouse


class BaseProxy():
  def __init__(self):
    self._keyboard = Keyboard()
    self._mouse = Mouse()
    self._screen = Screen()