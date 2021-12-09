import win32gui
import win32con
import os


class System:
  @staticmethod
  def do_nothing():
    pass
  
  def get_monitors():
    pass

  def get_open_apps(self):
    """Returns a list of tuples containing the window handle and name

    Returns:
        [list(tuple)]: list of window handles and names
    """
    apps = []

    def callback(hwnd, _):
      if (win32gui.IsWindowVisible(hwnd)):
        apps.append((hwnd, win32gui.GetWindowText(hwnd)))
  
    win32gui.EnumWindows(callback, None)
    return apps
  
  def get_app(self, name):
    return win32gui.FindWindowEx(0, 0, 0, name)
  
  def bring_app_to_front(self, hwnd):
    win32gui.SetForegroundWindow(hwnd)
  
  def focus_app(self, hwnd):
    win32gui.SetFocus(hwnd)
  
  def show_window_maximized(self, hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

  def show_window_normal(self, hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
  
  def show_window_maximized(self, hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
  
  def get_window_pos(self, hwnd):
    return win32gui.GetWindowRect(hwnd)
  
  def set_window_pos(self, hwnd, box):
    return

  def get_window_monitor(self, hwnd):
    box = self.get_window_pos(hwnd)
    print(box)
  
  def set_window_monitor(self, hwnd):
    pass

  def open_app(self, executeable_path):
    os.startfile('C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe')
