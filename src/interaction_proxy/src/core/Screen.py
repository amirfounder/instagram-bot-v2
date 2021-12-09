import mss
import numpy as np
import cv2 as cv
from PIL import Image
import pytesseract
from skimage.metrics import structural_similarity
from difflib import SequenceMatcher

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class Screen:

  def __init__(self, target_monitor=1) -> None:
    self.__sct = mss.mss()
    self._target_monitor = target_monitor

  def find_text(self, text, expected_occurences=1, confidence=.9):
    image = self.screenshot()
    self.save_numpy_image('image.png', image)
    boxes = self.find_text_from_image(image, text, confidence)

    if len(boxes) != expected_occurences:
      print(f'Expected to find the text: {text} {expected_occurences} times. But found {len(boxes)} times')
      return len(boxes), boxes
    
    if self._target_monitor == 1:
      return len(boxes), boxes
    
    new_boxes = []

    target_monitor_dimensions = self.__sct.monitors[self._target_monitor]
    left_offset = target_monitor_dimensions['left']
    top_offset = target_monitor_dimensions['top']

    for box in boxes:
      new_boxes.append((box[0] + left_offset, box[1] + top_offset, box[2], box[3]))

    return len(new_boxes), new_boxes

  def find_image(self, image, template):
    image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    width, height = template.shape[::-1]
    result = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8

    location = np.where(result >= threshold)
    boxes = []
    for pt in zip(*location[::-1]):
      boxes.append((pt[0], pt[1], width, height))
    
    return boxes

  def find_text_from_image(self, image, text:str, confidence=.9):
    data = pytesseract.image_to_data(image)
    data = [x.split('\t') for x in data.split('\n')]
    boxes = []

    for x in data:
      if len(x) == 12:
        similarity_score = self.build_similarity_score_between_text(x[11].lower(), text.lower())
        if similarity_score > confidence:
          left, top, width, height = x[6], x[7], x[8], x[9]
          boxes.append((int(left), int(top), int(width), int(height)))

    return boxes

  def build_similarity_score_between_text(self, textOne, textTwo):
    return SequenceMatcher(None, textOne, textTwo).ratio()

  def build_similarity_score_between_images(self, image_one, image_two):
    image_one_grayscale = cv.cvtColor(image_one, cv.COLOR_RGB2GRAY)
    image_two_grayscale = cv.cvtColor(image_two, cv.COLOR_RGB2GRAY)

    score, _ = structural_similarity(image_one_grayscale, image_two_grayscale, full=True)
    return score

  def screenshot(self, target_monitor=None):
    if target_monitor is None:
      target_monitor = self._target_monitor
    
    raw_pixels = self.__sct.grab(self.__sct.monitors[target_monitor])
    numpy_image = np.array(raw_pixels)
    numpy_image = cv.cvtColor(numpy_image, cv.COLOR_BGR2RGB)
    return numpy_image
  
  def save_numpy_image(self, filename, numpy_image):
    pillow_image = Image.fromarray(numpy_image)
    pillow_image.save(filename)
  
  def process_image_to_black_and_white(self, image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, black_and_white = cv.threshold(gray_image, 230, 255, cv.THRESH_BINARY)
    return black_and_white