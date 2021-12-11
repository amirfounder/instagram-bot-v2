from tkinter.font import Font, families
from src.utils import System
from tkinter import *


class Input:
  def __init__(self, root) -> None:
    self.__root = root
    self.__text = Entry(self.__root)
    self.__textvariable = StringVar()

    root = self.__root
    root.title("X Console")
    root.geometry('400x600+-500+20')

    on_key = root.register(self.on_key)
    on_return = root.register(self.on_return)

    text =self.__text
    text.grid(column=0, row=0)
    text.place(x=10, y=10, width=380, height=580)

    var = self.__textvariable

    font = Font(family='Terminal', size='9')
    text.configure(bd=0, bg='black', fg='white',font=font)
    text.configure(validate='all', validatecommand=(on_key, '%P'))
    text.configure(textvariable=var)

    root.mainloop()
  
  def validate(self, event):
    self.on_key()
    self.on_return()
  
  def on_key(self, event):
    print(event)
    self.on_return(event)
    return True
  
  def on_return(self, event):
    print(self.__textvariable)
    print(event)
    return True