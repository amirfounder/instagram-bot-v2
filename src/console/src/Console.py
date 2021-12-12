from src.console.src.components import Output
from tkinter import *
from src.console.src.components.ComponentGrid import ComponentGrid

from src.utils.system.src.system import System


class Console:
  def __init__(self) -> None:
    self.__title = 'XConsole'
    self.__system = System()
    self.__monitor = 3
    self.__root = Tk()
    self.__root.title(self.__title)

    self.configure_geometry()
    self.configure_styles()
    self.configure_component_grid()

    self.__root.after(250, self.move_to_monitor)
    self.__root.mainloop()

  def configure_geometry(self):
    _, _, w, h = self \
      .__system \
        .get_monitor(self.__monitor) \
          ['rect']

    self.__root_w = int(w / 1)
    self.__root_h = int(h / 1)
    self.__root.geometry(f'{self.__root_w}x{self.__root_h}')

  def move_to_monitor(self):
    hwnd = self.__system.get_open_app_by_name(self.__title)
    self.__system.move_app_to_monitor(hwnd, self.__monitor)
  
  def configure_styles(self):
    self.__root.config(bg='#222')

  def configure_component_grid(self):
    grid = ComponentGrid(self.__root, self.__root_w, self.__root_h)