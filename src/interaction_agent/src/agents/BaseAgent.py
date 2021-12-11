from src.interaction_agent.src.core import Keyboard, Screen, Mouse
from src.utils.system.src.System import System


class BaseAgent():
  def __init__(self):
    self._keyboard = Keyboard()
    self._mouse = Mouse()
    self._screen = Screen()
    self._system = System()