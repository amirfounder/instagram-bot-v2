from time import sleep
from src.interaction_proxy.src.core import Keyboard
from src.interaction_proxy.src.core import Mouse
from src.interaction_proxy.src.core import Screen

class InteractionProxy():

  def __init__(self):
    self.__keyboard = Keyboard()
    self.__mouse = Mouse()
    self.__screen = Screen(2)

  def setup_browser(self):
    monitor_1_screenshot_1 = self.__screen.screenshot(1)
    monitor_2_screenshot_1 = self.__screen.screenshot(2)

    self.__keyboard.press_and_release('windows')
    sleep(.2)
    self.__keyboard.write('brave')
    self.__keyboard.press_and_release('enter')
    sleep(.8)

    monitor_1_screenshot_2 = self.__screen.screenshot(1)
    monitor_2_screenshot_2 = self.__screen.screenshot(2)

    monitor_1_score = self.__screen.build_similarity_score(monitor_1_screenshot_1, monitor_1_screenshot_2)
    monitor_2_score = self.__screen.build_similarity_score(monitor_2_screenshot_1, monitor_2_screenshot_2)

    browser_monitor = 1 if monitor_2_score > monitor_1_score else 2

    if browser_monitor == 1:
      self.__keyboard.press('windows')
      self.__keyboard.press_and_release('left')
      self.__keyboard.press_and_release('left')
      self.__keyboard.press_and_release('left')
      self.__keyboard.press_and_release('up')
      self.__keyboard.press_and_release('up')
      self.__keyboard.press_and_release('up')
      self.__keyboard.release('windows')

    sleep(.3)
  
  def visit_url(self, url):
    self.__keyboard.press('ctrl')
    self.__keyboard.press_and_release('l')
    self.__keyboard.release('ctrl')
    self.__keyboard.write(url)
    self.__keyboard.press_and_release('enter')

  def close__current_tab(self):
    self.__keyboard.press('ctrl')
    self.__keyboard.press_and_release('w')
    self.__keyboard.release('ctrl')

  def research_hashtags(self):
    self.setup_browser()
    self.visit_url('https://instagram.com')

    sleep(3)
    
    box = self.__screen.find_text('search')
    if box is None:
      return
    
    self.__mouse.move_to_box(box)
    self.__mouse.click()
    sleep(1)
    self.__keyboard.write('#blue')
    sleep(2)
    self.__keyboard.backspace(len("#blue"))

    for word in ['#green', '#purple', "love"]:
      self.__keyboard.write(word)
      sleep(2)
      self.__keyboard.backspace(len(word))
      sleep(1)
    
    sleep(2)
    self.close__current_tab()