from time import sleep
from src.builders.script_builder.src.ScriptBuilder import ScriptBuilder
from src.interaction_proxy.src.proxies import BaseProxy
from pyperclip import copy, paste
from src.utils.constants import *


class BrowserProxy(BaseProxy):
  def __init__(self, browser: str=None):
    super().__init__()
    self._script_builder = ScriptBuilder()
    self._browser = browser
    self._browser_executeable = None
    
    self.__dev_tools_is_open = False
    self.__browser_is_open = False
    self.__browser_hwnd = None

    if (type(browser) == str and browser.lower() == 'brave') or browser == BRAVE_EXECUTEABLE:
      self._browser = 'brave'
      self._browser_executeable = BRAVE_EXECUTEABLE
      self._browser_app_name_ext = ' - Brave'
    if (type(browser) == str and browser.lower() == 'chrome') or browser == CHROME_EXECUTEABLE:
      self._browser = 'chrome'
      self._browser_executeable = CHROME_EXECUTEABLE
      self._browser_app_name_ext = ' - Google Chrome'

    if self._browser_executeable is None:
      print("INFO: You have created an instance of BrowserProxy without specifiying a browser. Defaulting to Brave")
      self._browser = 'brave'
      self._browser_executeable = BRAVE_EXECUTEABLE
      self._browser_app_name_ext = ' - Brave'

  def _open_browser(self, monitor=1, maximize=True):
    if not self.__browser_is_open:
      self._system.open_app(BRAVE_EXECUTEABLE)
      sleep(.5)
      self.__browser_hwnd = self._system.get_foreground_app()[0]

    self._system.move_app_to_monitor(self.__browser_hwnd, monitor, maximize)
    if maximize:
      self._system.show_app_maximized(self.__browser_hwnd)
      
    self.__browser_is_open = True

  def _close_browser(self):
    if self.__browser_is_open:
      self._system.close_app(self.__browser_hwnd)
      self.__browser_is_open = False

  def _navigate_to_url(self, url):
    self._keyboard.press('ctrl')
    self._keyboard.press_and_release('l')
    self._keyboard.release('ctrl')
    sleep(.3)
    self._keyboard.write(url, .001)
    sleep(.3)
    self._keyboard.press_and_release('enter')

  def _toggle_dev_tools_console(self):
    self._keyboard.press('ctrl')
    self._keyboard.press('shift')
    self._keyboard.press_and_release('j')
    self._keyboard.release('shift')
    self._keyboard.release('ctrl')
    self.__dev_tools_is_open = not self.__dev_tools_is_open

  def _open_dev_tools_console(self):
    if not self.__dev_tools_is_open:
      self._toggle_dev_tools_console()
      sleep(.5)

    self._focus_dev_tools()
    sleep(.5)
  
  def _close_dev_tools_console(self):
    if self.__dev_tools_is_open:
      self._toggle_dev_tools_console()
      sleep(.5)

  def _focus_dev_tools(self):
    self._keyboard.press('ctrl')
    self._keyboard.press_and_release('`')
    self._keyboard.release('ctrl')

  def _execute_dev_tools_console_script(self, script):
    self._focus_dev_tools()
    copy(script)
    self._keyboard.press('ctrl')
    self._keyboard.press_and_release('v')
    self._keyboard.release('ctrl')
    sleep(.1)
    self._keyboard.press_and_release('enter')

  def _wait_until_webpage_loaded(self):
    loaded = False

    while (not loaded):
      for i in range(3):
        sleep(1)
        loaded = self._is_webpage_loaded()
        if loaded:
          return
      self._keyboard.press('ctrl')
      self._keyboard.press_and_release('r')
      self._keyboard.release('ctrl')

  def _is_webpage_loaded(self):
    if not self.__browser_is_open:
      print('browser is not open. refusing to check webpage loading status')

    self._open_dev_tools_console()
    script = self._script_builder.build_get_loading_state_script()
    self._execute_dev_tools_console_script(script)
    self._close_dev_tools_console()
    sleep(1.25)
    return paste() == 'complete'

  def _close_browser(self):
    self._system.close_app(self.__browser_hwnd)
