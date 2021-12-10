import string


class JavascriptBuilder():

  def __init__(self) -> None:
    self.instagram_search_element_class_selector = 'QY4Ed'
    self.js_variables_in_use = []

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

  def __build_find_element_matching_class(self, css_class):
    js_variable = self.__build_unique_js_variable_name()
    return f'{js_variable}=document.querySelector(".{css_class}");'
  
  def __build_find_element_matching_id(self, css_id):
    js_variable = self.__build_unique_js_variable_name()
    return f'{js_variable}=document.querySelector("#{css_id}");'

  def build_modify_instagram_search_box_styles_script(self):
    class_selector = self.instagram_search_element_class_selector
    variable_assignment_script = self.__build_find_element_matching_class(class_selector)
    variable = variable_assignment_script[:2]
    style_change_script = \
      f'{variable_assignment_script}' \
        f'Array.from({variable}.querySelectorAll("*"))' \
          '.forEach(x => {' \
            'x.style.fontWeight=800;' \
              'x.style.color="black";' \
                'x.style.fontSize="20px";' \
                  '})'
    
    return style_change_script

  def build_get_loading_state_script(self, timeout_duration=1000):
    return f'setTimeout(async()=>await window.navigator.clipboard.writeText(document.readyState),{timeout_duration})'
