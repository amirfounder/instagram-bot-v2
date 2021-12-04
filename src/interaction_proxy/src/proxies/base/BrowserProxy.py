from src.interaction_proxy.src.proxies.base import BaseProxy
from time import sleep


class BrowserProxy(BaseProxy):
  def __init__(
    self,
    browser_name='brave'
  ):
    super().__init__()
    self._browser_name = browser_name

  def open_browser(self):
    self._keyboard.press_and_release('windows')
    sleep(.3)
    self._keyboard.write(self._browser_name, 0.01)
    sleep(.2)
    self._keyboard.press_and_release('enter')

  def open_browser_on_monitor(self, target_monitor=None):
    monitor_1_screenshot_1 = self._screen.screenshot(1)
    monitor_2_screenshot_1 = self._screen.screenshot(2)
    
    self.open_browser()
    sleep(.3)
    
    monitor_1_screenshot_2 = self._screen.screenshot(1)
    monitor_2_screenshot_2 = self._screen.screenshot(2)
    monitor_1_similarity_score = self._screen.build_similarity_score(monitor_1_screenshot_1, monitor_1_screenshot_2)
    monitor_2_similarity_score = self._screen.build_similarity_score(monitor_2_screenshot_1, monitor_2_screenshot_2)
    
    current_browser_monitor = 1 if monitor_2_similarity_score > monitor_1_similarity_score else 2

    if target_monitor is None or \
      current_browser_monitor == target_monitor:
      return
    
    self.move_browser_to_window(current_browser_monitor, target_monitor)

  def move_browser_to_window(self, current_monitor, target_monitor):
    # TODO Check the system to identify the order of the monitors
    # TODO Extend support beyond two monitors

    self._keyboard.press('windows')

    for _ in range(3):
      if current_monitor == 1 and target_monitor == 2:
        self._keyboard.press_and_release('left')
      else:
        self._keyboard.press_and_release('right')
    
    self._keyboard.press_and_release('up')
    self._keyboard.press_and_release('up')
    self._keyboard.press_and_release('up')
    self._keyboard.release('windows')

  def navigate_to_url(self, url):
    self._keyboard.press('ctrl')
    self._keyboard.press_and_release('l')
    self._keyboard.release('ctrl')
    sleep(.3)
    self._keyboard.write(url, .01)
    sleep(.3)
    self._keyboard.press_and_release('enter')

  def open_dev_tools_console(self):
    self._keyboard.press('ctrl')
    self._keyboard.press('shift')
    self._keyboard.press_and_release('j')
    self._keyboard.release('shift')
    self._keyboard.release('ctrl')
    
    sleep(.5)

    self._keyboard.press('ctrl')
    self._keyboard.press_and_release('`')
    self._keyboard.release('ctrl')

  def run_dev_tools_console_script(self, script):
    self._keyboard.write(script, 0.001)
    self._keyboard.press_and_release('enter')

  def build_script_to_modify_instagram_search_input(self):
    return \
    "Array.from(document.querySelectorAll('*'))" + \
    ".filter(x => x.textContent.toLowerCase().includes('search'))" + \
    ".filter(x => !['html', 'body'].includes(x.tagName.toLowerCase()))" + \
    ".slice(3)" + \
    ".forEach(x => {" + \
    "x.style.fontWeight = '500';" + \
    "x.style.color = 'black';" + \
    "x.style.fontSize = '20px';" + \
    "})"
