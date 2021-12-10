import win32gui
import win32con
import win32api
import os


class System:
  @staticmethod
  def do_nothing():
    pass
  
  def get_monitors(self):
    monitors = []
    i = 1

    for h_monitor, _, _ in win32api.EnumDisplayMonitors():
      monitor_info = win32api.GetMonitorInfo(h_monitor)
      monitors.append({
        'rect': monitor_info['Monitor'],
        'device': monitor_info['Device'],
        'display': i,
        'flags': monitor_info['Flags']
      })
      i += 1
    
    return monitors

  def get_monitor(self, display=1):
    monitors = self.get_monitors()
    return [x for x in monitors if x['display'] == display][0]

  def get_open_apps(self):
    apps = []

    def callback(hwnd, _):
      if (win32gui.IsWindowVisible(hwnd)):
        apps.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(callback, None)
    return apps
  
  def get_open_app(self, name):
    return win32gui.FindWindowEx(0, 0, 0, name)

  def move_app_to_front(self, hwnd):
    win32gui.SetForegroundWindow(hwnd)
  
  def focus_app(self, hwnd):
    win32gui.SetFocus(hwnd)

  def open_app(self, executeable_path):
    os.startfile(executeable_path)

  def show_app_maximized(self, hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

  def show_app_normal(self, hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
  
  def show_app_maximized(self, hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
  
  def move_app_to_monitor(self, hwnd, monitor_id, maximize=False):
    current_monitor = self.get_app_monitor(hwnd)
    target_monitor = self.get_monitor(monitor_id)

    if current_monitor['display'] == target_monitor['display']:
      return

    current_x, current_y, current_monitor_width, current_monitor_height = current_monitor['rect']
    x, y, target_monitor_width, target_monitor_height = target_monitor['rect']

    if current_monitor_width == 0:
      current_monitor_width = abs(current_x)
    
    if current_monitor_height == 0:
      current_monitor_height = abs(current_y)
    
    if target_monitor_width == 0:
      target_monitor_width = abs(x)
    
    if target_monitor_height == 0:
      target_monitor_height = abs(y)
    
    x_scale = target_monitor_width / current_monitor_width
    y_scale = target_monitor_height / current_monitor_height

    _, _, app_width, app_height = self.get_app_pos(hwnd)

    scaled_width = int(app_width * x_scale)
    scaled_height = int(app_height * y_scale)

    width = target_monitor_width if maximize else scaled_width
    height = target_monitor_height if maximize else scaled_height 

    win32gui.MoveWindow(hwnd, x, y, width, height, True)

  def get_app_pos(self, hwnd):
    x, y, right, bottom = win32gui.GetWindowRect(hwnd)
    width = abs(x - right)
    height = abs(bottom - y)

    return x, y, width, height
  
  def get_app_monitor(self, hwnd):
    monitors = self.get_monitors()
    app_rect = self.get_app_pos(hwnd)
    app_start_point = app_rect[0]

    monitors = sorted(monitors, key = lambda x: x['rect'][0])
    app_monitor = None

    for monitor in monitors:
      monitor_start_point = monitor['rect'][0]
      if app_start_point > monitor_start_point:
        app_monitor = monitor

    return app_monitor
  