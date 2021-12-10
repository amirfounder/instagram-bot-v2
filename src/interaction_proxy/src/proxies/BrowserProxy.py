from time import sleep
from src.interaction_proxy.src.proxies import BaseProxy
from src.utils.constants import *


class BrowserProxy(BaseProxy):
  def __init__(self, browser: str=None):
    super().__init__()
    self._browser = browser
    self._browser_executeable = None

    if (type(browser) == str and browser.lower() == 'brave') or browser == BRAVE_EXECUTEABLE:
      self._browser_executeable = BRAVE_EXECUTEABLE
    if (type(browser) == str and browser.lower() == 'chrome') or browser == CHROME_EXECUTEABLE:
      self._browser_executeable = CHROME_EXECUTEABLE

    if self._browser_executeable is None:
      print("INFO: You have created an instance of BrowserProxy without specifiying a browser. Defaulting to Brave")
      self._browser = 'brave'
      self._browser_executeable = BRAVE_EXECUTEABLE

  def _open_browser(self, monitor=1, maximize=True):
    self._system.open_app(BRAVE_EXECUTEABLE)
    sleep(.5)
    app = self._system.get_foreground_app()[0]

    self._system.move_app_to_monitor(app, monitor, maximize)
    if maximize:
      self._system.show_app_maximized(app)

  def _navigate_to_url(self, url):
    self._keyboard.press('ctrl')
    self._keyboard.press_and_release('l')
    self._keyboard.release('ctrl')
    sleep(.3)
    self._keyboard.write(url, .001)
    sleep(.3)
    self._keyboard.press_and_release('enter')

  def _open_dev_tools_console(self):
    self._keyboard.press('ctrl')
    self._keyboard.press('shift')
    self._keyboard.press_and_release('j')
    self._keyboard.release('shift')
    self._keyboard.release('ctrl')
    
    sleep(.5)

    self._keyboard.press('ctrl')
    self._keyboard.press_and_release('`')
    self._keyboard.release('ctrl')

  def _run_dev_tools_console_script(self, script):
    self._keyboard.write(script, 0.001)
    self._keyboard.press_and_release('enter')
