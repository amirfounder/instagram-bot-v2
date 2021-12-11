from tkinter import *
from src.data_manager import FileManager, DatabaseManager


class Output(Frame):
  def __init__(self, root) -> None:
    super().__init__(master=root)
    self.__database_manager = DatabaseManager()
    self.__file_manager = FileManager()
    
    self.configure_styles()

  def configure_styles(self):
    self.configure(bg='black')
  
  def log_to_console(self):
    pass