class JavascriptBuilder():

  def build_alter_font_of_element_by_id_function_(self, id, weight=500, size=20, color='black'):
    return "const alterFontOfElementById = (id) => {" \
    f"const element = document.getElementById({id});" \
    f"x.style.fontWeight = '{weight}';" + \
    f"x.style.color = '{color}';" + \
    f"x.style.fontSize = '{size}px';" + \
    "}" \

  def build_alter_font_of_element_with_text_function(self, weight=500, size=20, color='black'):
    return "const alterFontOfElementWithText = () => {" \
    "Array.from(document.querySelectorAll('*'))" \
    ".filter(x => x.textContent.toLowerCase().includes('search'))" \
    ".filter(x => !['html', 'body'].includes(x.tagName.toLowerCase()))" + \
    ".slice(3)" + \
    ".forEach(x => {" + \
    f"x.style.fontWeight = '{weight}';" + \
    f"x.style.color = '{color}';" + \
    f"x.style.fontSize = '{size}px';" + \
    "})" \
    "}"
  
  def build_get_parents_function():
    return "const getParents = (node) => {" \
    "target = node;" \
    "parents = [];" \
    "while (target) {" \
    "parents.unshif(target);" \
    "target = target.parentElement;" \
    "}" \
    "}"