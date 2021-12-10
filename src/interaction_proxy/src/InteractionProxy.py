from time import sleep
from src.interaction_proxy.src.core import Keyboard
from src.interaction_proxy.src.core import Mouse
from src.interaction_proxy.src.core import Screen
from src.interaction_proxy.src.proxies import InstagramProxy

class InteractionProxy(InstagramProxy):

  def __init__(self):
    self.__keyboard = Keyboard()
    self.__mouse = Mouse()
    self.__screen = Screen(2)

  def open_browser_dev_tools(self):
    self.__keyboard.press('ctrl')
    self.__keyboard.press('shift')
    self.__keyboard.press_and_release('j')
    self.__keyboard.release('shift')
    self.__keyboard.release('ctrl')
    sleep(1)

    self.__keyboard.press('ctrl')
    self.__keyboard.press_and_release('`')
    self.__keyboard.release('ctrl')

  def write_script_to_modify_instagram_search_text_input(self):
    codeblock = \
    "Array.from(document.querySelectorAll('*'))" + \
    ".filter(x => x.textContent.toLowerCase().includes('search'))" + \
    ".filter(x => !['html', 'body'].includes(x.tagName.toLowerCase()))" + \
    ".slice(3)" + \
    ".forEach(x => {" + \
    "x.style.fontWeight = '500';" + \
    "x.style.color = 'black';" + \
    "x.style.fontSize = '20px';" + \
    "})"

    self.__keyboard.write(codeblock, 0.01)
    self.__keyboard.press_and_release('enter')
    print('pressed enter')

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

    monitor_1_score = self.__screen.build_similarity_score_between_images(monitor_1_screenshot_1, monitor_1_screenshot_2)
    monitor_2_score = self.__screen.build_similarity_score_between_images(monitor_2_screenshot_1, monitor_2_screenshot_2)

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
    self.__keyboard.write(url, 0.01)
    self.__keyboard.press_and_release('enter')

  def close__current_tab(self):
    self.__keyboard.press('ctrl')
    self.__keyboard.press_and_release('w')
    self.__keyboard.release('ctrl')

  def research_hashtags(self):
    self.setup_browser()
    self.visit_url('https://instagram.com')

    sleep(2)

    self.open_browser_dev_tools()
    self.write_script_to_modify_instagram_search_text_input()
    
    sleep(1)
    
    box = self.__screen.find_text('search')
    if box is None:
      return
    
    self.__mouse.move_to_box(box)
    self.__mouse.click()
    sleep(1)
    self.__keyboard.write('#blue')
    sleep(2)
    self.__keyboard.backspace(len("#blue"))

    # for word in ['#green', '#purple', "#love"]:
    #   self.__keyboard.write(word)
    #   sleep(2)
    #   self.__keyboard.backspace(len(word))
    #   sleep(1)
    
    self.__mouse.click("middle")
    self.__mouse.move((0, 20))
    sleep(2)
    self.__mouse.click("middle")
    
    sleep(2)
    self.close__current_tab()