from datetime import datetime
from pynput import mouse, keyboard
from threading import Thread
import os


class MyException(Exception):
  pass


class InteractionLogger:
  
  _root_log_directory = 'C:\\x\\logs\\interaction-logger'
  _max_log_file_size = 50 * 1000 * 1000
  _kill_key_one = keyboard.Key.shift_r
  _kill_key_two = keyboard.Key.ctrl_r

  _kill_key_one_pressed = False
  _kill_key_two_pressed = False
  _kill_logger = False

  _mouse_press_event_type = 'mp'
  _mouse_release_event_type = 'mr'
  _mouse_move_event_type = 'mm'
  _mouse_scoll_event_type = 'ms'
  _key_press_event_type = 'kp'
  _key_release_event_type = 'kr'

  def __init__(self):
    directories = self._root_log_directory.split('\\')
    current = ''
    for directory in directories:
      current += directory if current == '' else f'\\{directory}'
      if not os.path.isdir(current):
        os.mkdir(current)

  def run(self):
    thread_one = Thread(target=self.run_keyboard_listener)
    thread_two = Thread(target=self.run_mouse_listener)

    thread_one.start()
    thread_two.start()

  def on_mouse_click(self, x, y, button, pressed):
    event_type = (
      self._mouse_release_event_type,
      self._mouse_press_event_type
    )[pressed]
    button = ('r', 'l')[button == mouse.Button.left]
    event = f'{event_type},{x},{y},{button}'
    self.log_event(event)
    self.handle_potential_kill(event_type)

  def on_mouse_move(self, x, y):
    event = f'{self._mouse_move_event_type},{x},{y}'
    self.log_event(event)
    self.handle_potential_kill(self._mouse_move_event_type)

  def on_mouse_scroll(self, x, y, dx, dy):
    event = f'{self._mouse_scoll_event_type},{x},{y},{dx},{dy}'
    self.log_event(event)
    self.handle_potential_kill(self._mouse_scoll_event_type)

  def on_key_press(self, key):
    event = f'{self._key_press_event_type},{key}'
    self.log_event(event)
    self.handle_potential_kill(self._key_press_event_type, key)

  def on_key_release(self, key):
    event = f'{self._key_release_event_type},{key}'
    self.log_event(event)
    self.handle_potential_kill(self._key_release_event_type, key)

  def handle_potential_kill(self, event_type, event_value=None):
    if event_type == self._key_press_event_type:
      if event_value == self._kill_key_one:
        self._kill_key_one_pressed = True
      if event_value == self._kill_key_two:
        self._kill_key_two_pressed = True

    if event_type == self._key_release_event_type:
      if event_value == self._kill_key_one:
        self._kill_key_one_pressed = False
      if event_value == self._kill_key_two:
        self._kill_key_two_pressed = False
    
    if self._kill_key_two_pressed and self._kill_key_two_pressed:
      self._kill_logger = True
    else:
      self._kill_logger = False

    if self._kill_logger:
      raise MyException()
   
  def log_event(self, event, version='1'):
    timestamp = self.get_timestamp()
    target_log_file = self.build_log_file()

    version_tag = f'v{version}'
    timestamp_tag = f't{timestamp}'

    data = ','.join([version_tag, timestamp_tag, event])
    
    f = open(target_log_file, 'a')
    f.write(data + '\n')
    f.close()

  def build_log_file(self):
    today = datetime.now().strftime(r'%Y_%m_%d')
    target_directory = self._root_log_directory + f'\\{today}'
    directory_exists = os.path.isdir(target_directory)
    target_file_name = '1.log'

    if directory_exists:
      files = os.listdir(target_directory)
      files_count = len(files)

      if files_count > 0:
        last_file = files[files_count - 1]
        last_file_size = os.path.getsize(target_directory + f'\\{last_file}')

        if last_file_size >= self._max_log_file_size:
          target_file_name = f'{files_count + 1}.log'
        else:
          target_file_name = last_file
    else:
      os.mkdir(target_directory)
    
    return target_directory + f'\\{target_file_name}'

  def get_today(self):
    return datetime.now().strftime(r'%Y_%m_%d')

  def get_timestamp(self):
    return datetime.now().strftime(r'%H_%M_%S_%f')

  def run_keyboard_listener(self):
    with keyboard.Listener(
      on_press=self.on_key_press,
      on_release=self.on_key_release,
    ) as listener:
      try:
        listener.join()
      except MyException:
        print('stopping')

  def run_mouse_listener(self):
    with mouse.Listener(
      on_click=self.on_mouse_click,
      on_scroll=self.on_mouse_scroll,
      on_move=self.on_mouse_move
    ) as listener:
      try:
        listener.join()
      except MyException:
        print('stopping')
