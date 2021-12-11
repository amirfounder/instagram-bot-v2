import os
import re
from time import sleep
from src.interaction_proxy.src.proxies import BrowserProxy
from pyperclip import paste

from src.utils.enums.colors import Color


class InstagramProxy(BrowserProxy):
  def __init__(self, browser=None, target_monitor=None, username=None):
    super().__init__(browser=browser)
    self._screen._target_monitor = target_monitor or 2
    self._username = username

  def research_hashtags(self):
    script = self._script_builder.build_modify_instagram_search_box_styles_script()
    self._open_dev_tools_console()
    self._execute_dev_tools_console_script(script)
    self._close_dev_tools_console()

  def click_search_input(self):
    box = self._screen.find_text('search')
    if box is None:
      self.stop()
    
    self._mouse.move_to_box(box)
    self._mouse.click()

  def is_on_login_continue_page(self):
    var, select_username_script = self._script_builder.build_select_login_continue_as_button_script()
    copy_script = self._script_builder.build_copy(var)
    self._execute_dev_tools_console_script(select_username_script)
    self._execute_dev_tools_console_script(copy_script)
    return paste() != 'undefined'
    
  def is_on_login_fresh_page(self):
    var, select_script = self._script_builder.build_select_login_username_script()
    copy_script = self._script_builder.build_copy(var)
    self._execute_dev_tools_console_script(select_script)
    self._execute_dev_tools_console_script(copy_script)
    return paste() != 'undefined'

  def logout(self):
    var, script = self._script_builder.build_select_profile_picture_script(self._username)
    self._open_dev_tools_console()
    self._focus_dev_tools()
    self._execute_dev_tools_console_script(script)
    script = self._script_builder.build_click_element_script(var)
    self._execute_dev_tools_console_script(script)
    sleep(.5)
    var, script = self._script_builder.build_select_logout_link_script()
    self._execute_dev_tools_console_script(script)
    script = self._script_builder.build_click_element_script(var)
    self._execute_dev_tools_console_script(script)
  
  def login(self):
    on_login_fresh_page = self.is_on_login_fresh_page()
    on_login_continue_page = self.is_on_login_continue_page()

    if on_login_continue_page and on_login_fresh_page:
      print('there was a problem...')
    
    if not on_login_continue_page and not on_login_fresh_page:
      print('you must be already logged in...')
    
    if on_login_fresh_page:
      self.login_from_fresh_page()
    
  
  def login_from_fresh_page(self):
    username_input, select_username_script = \
      self._script_builder.build_select_login_username_script()
    password_input, select_password_script = \
      self._script_builder.build_select_login_password_script()
    login_button, select_login_button_script = \
      self._script_builder.build_select_login_login_button_script()
    
    self._execute_dev_tools_console_script(select_username_script)
    self._execute_dev_tools_console_script(select_password_script)
    self._execute_dev_tools_console_script(select_login_button_script)

    clear_all_attributes_script = \
      self._script_builder.build_clear_all_attributes([
        username_input,
        password_input,
        login_button
      ])
    
    self._execute_dev_tools_console_script(clear_all_attributes_script)

    styles = { 'fontSize': '30px', 'padding': '20px'}
    script = self._script_builder.build_modify_styles_of_element(username_input, styles)
    script += self._script_builder.build_modify_styles_of_element(password_input, styles)
    script += self._script_builder.build_modify_styles_of_element(login_button, styles)
    self._execute_dev_tools_console_script(script)

    styles = { 'backgroundColor': 'rgb(255, 0, 0)' }
    script = self._script_builder.build_modify_styles_of_element(username_input, styles)
    self._execute_dev_tools_console_script(script)
    img = self._screen.screenshot()
    box = self._screen.find_color_on_image(img, Color.RED)
    monitor = self._system.get_monitor(2)
    mx, _, _, _ = monitor['rect']
    bx, y, w, h = box
    box = (bx + mx, y, w, h)
    self._mouse.move_to_box(box, spacing=10)
    self._mouse.click()
    sleep(.5)
    self._keyboard.write('liamsmith65843')
    self._keyboard.press_and_release('esc')


  def start(self):
    self._open_browser(2)
    self._navigate_to_url('https://instagram.com')
    self._wait_until_webpage_loaded()

  def stop(self):
    self._keyboard.hotkey(['alt', 'f4'])