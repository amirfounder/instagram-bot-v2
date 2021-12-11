from tkinter import *


class ComponentGrid(Frame):
  def __init__(self, root, x, y) -> None:
    super().__init__(master=root)
    # self.configure(bg='white')
    self.configure_components()
  
  def configure_components(self):
    self.grid_columnconfigure(index=0, minsize=50, pad=3)
    self.grid_rowconfigure(index=0, minsize=50, pad=3)
    # self.columnconfigure(0)
    # self.columnconfigure(1)
    # self.columnconfigure(2)
    # self.columnconfigure(3)
    # self.rowconfigure(0)
    # self.rowconfigure(1)

    # text = Text(self)
    # text.grid(row=0, columnspan=1)