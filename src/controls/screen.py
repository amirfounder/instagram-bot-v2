import mss
import numpy as np
import cv2 as cv
import pytesseract
from numpy import ndarray
from skimage.metrics import structural_similarity
from difflib import SequenceMatcher

from src.data.files import save_numpy_array_to_image
from src.utils.enums import Color

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
sct = mss.mss()

TARGET_MONITOR = 1


def find_text(text, expected_occurences=1, confidence=.9):
    image = screenshot()
    save_numpy_array_to_image('image.png', image)
    boxes = find_text_from_image(image, text, confidence)

    if len(boxes) != expected_occurences:
        return len(boxes), boxes

    if TARGET_MONITOR == 1:
        return len(boxes), boxes

    new_boxes = []

    target_monitor_dimensions = sct.monitors[TARGET_MONITOR]
    left_offset = target_monitor_dimensions['left']
    top_offset = target_monitor_dimensions['top']

    for box in boxes:
        new_boxes.append(
            (box[0] + left_offset, box[1] + top_offset, box[2], box[3]))

    return len(new_boxes), new_boxes


def find_image(image, template):
    image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    width, height = template.shape[::-1]
    result = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8

    location = np.where(result >= threshold)
    boxes = []
    for pt in zip(*location[::-1]):
        boxes.append((pt[0], pt[1], width, height))

    return boxes


def find_text_from_image(image: ndarray, text: str, confidence=.9):
	data = pytesseract.image_to_data(image)
	data: list[str] = [x.split('\t') for x in data.split('\n')]
	boxes = []

	for row in data:
		if len(row) == 12:
			t1 = row[11].lower()
			t2 = text.lower()

			sim_score = get_texts_similarity_score(t1, t2)

			if sim_score > confidence:
				x, y, width, height = row[6], row[7], row[8], row[9]
				boxes.append((int(x), int(y), int(width), int(height)))

	return boxes


def get_texts_similarity_score(textOne, textTwo):
    return SequenceMatcher(None, textOne, textTwo).ratio()


def get_image_similarity_score(image_one, image_two):
    image_one_grayscale = cv.cvtColor(image_one, cv.COLOR_RGB2GRAY)
    image_two_grayscale = cv.cvtColor(image_two, cv.COLOR_RGB2GRAY)

    score, _ = structural_similarity(
        image_one_grayscale,
		image_two_grayscale,
		full=True
	)

    return score


def find_color_on_image(image: ndarray, color: Color):
    lower = None
    upper = None

    if color is Color.RED:
        lower = np.array([200, 0, 0], dtype='uint8')
        upper = np.array([255, 50, 50], dtype='uint8')
    else:
        return

    mask = cv.inRange(image, lower, upper)
    contours, _ = cv.findContours(mask, 1, 1)

    x, y, w, h = cv.boundingRect(
        [x for x in contours if cv.contourArea(x) > 2000][0])
    return int(x), int(y), int(w), int(h)


def screenshot(target_monitor=None):
    if target_monitor is None:
        target_monitor = TARGET_MONITOR

    raw_pixels = sct.grab(sct.monitors[target_monitor])
    numpy_image = np.array(raw_pixels)
    numpy_image = cv.cvtColor(numpy_image, cv.COLOR_BGR2RGB)
    return numpy_image
