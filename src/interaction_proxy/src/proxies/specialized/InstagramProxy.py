import os
from time import sleep
from src.interaction_proxy.src.proxies.base import BrowserProxy


class InstagramProxy(BrowserProxy):
  def __init__(self, browser_name='brave'):
    super().__init__(browser_name=browser_name)
    self._screen._target_monitor = 2

  def click_search_input(self):
    box = self._screen.find_text('search')
    if box is None:
      self.shutdown()
    
    self._mouse.move_to_box(box)
    self._mouse.click()

  def run(self):
    self.open_browser_on_monitor(2)
    self.navigate_to_url('instagram.com')
    
    sleep(2)
    
    self.open_dev_tools_console()

    script = self.build_script_to_modify_instagram_search_input()
    self.run_dev_tools_console_script(script)

    sleep(.3)

    self.click_search_input()
  
  def shutdown(self):
    os.exit()