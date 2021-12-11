import string


class JavascriptBuilder():

  def __init__(self) -> None:
    self.js_variables_in_use = []

    self.instagram_search_element_selector = '.QY4Ed'
    self.instagram_user_profile_menu_items_selector = '.-qQT3'

    self.instagram_login_password_input_selector = 'input[aria-label=\'Password\']'
    self.instagram_login_username_input_selector = 'input[aria-label=\'Phone number, username, or email\']'
    self.instagram_login_login_button_selector = 'button[type=\'submit\']'
    self.instagram_login_continue_as_button_selector = 'button'


  def __build_unique_js_variable_name(self):
    alphabet = list(string.ascii_lowercase)
    unique_js_variable_name = None

    for first_letter in alphabet:
      for second_letter in alphabet:
        potential_variable_name = f'{first_letter}{second_letter}'
        if potential_variable_name not in self.js_variables_in_use:
          unique_js_variable_name = potential_variable_name
          break
      if unique_js_variable_name is not None:
        break
    
    if unique_js_variable_name is None:
      raise Exception("Reached the limit of unique JS variable names. Please update code!")

    self.js_variables_in_use.append(unique_js_variable_name)
    return unique_js_variable_name

  def build_query_selector_script(self, selector):
    js_variable = self.__build_unique_js_variable_name()
    return js_variable, f'{js_variable}=document.querySelector("{selector}");'
  
  def build_query_selector_all_script(self, selector):
    js_variable = self.__build_unique_js_variable_name()
    return js_variable, f'{js_variable}=document.querySelector("{selector}");'
  
  def build_click_element_script(self, js_variable):
    return f'{js_variable}.click()'


  def build_select_profile_picture_script(self, username):
    return self.build_query_selector_script(f'img[alt="{username}\'s profile picture"]')
  
  def build_select_logout_link_script(self):
    selector = self.instagram_user_profile_menu_items_selector
    variable, selector_script = self.build_query_selector_all_script(selector)
    script = \
    f'{selector_script}' \
    f'{variable} = Array.from({variable})' \
    '.filter(x => x.textContent.toLowerCase().includes("log out"))[0]'
    return variable, script
  

  def build_select_login_username_script(self):
    selector = self.instagram_login_username_input_selector
    return self.build_query_selector_script(selector)
  
  def build_select_login_password_script(self):
    selector = self.instagram_login_password_input_selector
    return self.build_query_selector_script(selector)

  def build_select_login_login_button_script(self):
    selector = self.instagram_login_login_button_selector
    return self.build_query_selector_script(selector)

  def build_select_login_continue_as_button_script(self):
    selector = self.instagram_login_login_button_selector
    var, script = self.build_query_selector_all_script(selector)
    return var, \
    f'{script}' \
    f'{var} = Array.from({var})' \
    '.filter(x => x.textContent.toLowerCase().includes(\'continue as\'))[0]'


  def build_modify_instagram_search_box_styles_script(self):
    selector = self.instagram_search_element_selector
    variable, selector_script = self.build_query_selector_script(selector)
    script = \
    f'{selector_script}' \
    f'Array.from({variable}.querySelectorAll("*"))' \
    '.forEach(x => {' \
    'x.style.fontWeight=800;' \
    'x.style.color="black";' \
    'x.style.fontSize="20px";' \
    '})'
    return script


  def build_copy(self, js_expression):
    return f'copy({js_expression})'

  def build_copy_ready_state_script(self):
    return 'copy(document.readyState)'
