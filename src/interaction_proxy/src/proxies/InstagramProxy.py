import os
from time import sleep
from src.interaction_proxy.src.proxies import BrowserProxy


class InstagramProxy(BrowserProxy):
  def __init__(self, browser=None, target_monitor=None):
    super().__init__(browser=browser)
    self._screen._target_monitor = target_monitor or 2

  def start(self):
    self._open_browser(2)
    self._navigate_to_url('https://instagram.com')
    self._wait_until_webpage_loaded()

  def research_hashtags(self):
    script = self._script_builder.build_modify_instagram_search_box_styles_script()
    self._open_dev_tools_console()
    self._execute_dev_tools_console_script(script)
    self._close_dev_tools_console()

  def click_search_input(self):
    box = self._screen.find_text('search')
    if box is None:
      self.shutdown()
    
    self._mouse.move_to_box(box)
    self._mouse.click()

  def run(self):
    self.open_browser(2)
    self.navigate_to_url('instagram.com')
    
    sleep(2)
    
    self.open_dev_tools_console()
    sleep(3)
    count, boxes = self._screen.find_text('application')
    if count == 0:
      return

    self._mouse.move_to_box(boxes[0])
    self._mouse.click()

    sleep(.5)

    count, boxes = self._screen.find_text('cookies')
    if count == 0:
      return
    
    for box in boxes:
      self._mouse.move_to_box(box)
      self._mouse.click()
      self._mouse.click()

    sleep(.5)

    count, boxes = self._screen.find_text('https://www.instagram.com')
    if count == 0:
      return

    self._mouse.move_to_box(boxes[0])
    self._mouse.click("right")
    self._mouse.move((20, 20))
    self._mouse.click()
    self._keyboard.press('ctrl')
    self._keyboard.press_and_release('r')
    self._keyboard.release('ctrl')

    # script = self.build_script_to_modify_instagram_search_input()
    # self.run_dev_tools_console_script(script)

    # sleep(.3)

    # self.click_search_input()

    # username = 'liamsmith65843'
    # self.navigate_to_url(f'https://instagram.com/{username}')
    # sleep(2)
  
  def shutdown(self):
    os.exit()