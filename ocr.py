import cv2
import glob
import numpy as np
import pytesseract
from PIL import Image
import cv2
import numpy as np
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
for img1 in glob.glob("C:\\Users\\Vamsi\\Desktop\\ser\\sample\\*.JPG"):
	img = cv2.imread(img1)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
	contours = cv2.findContours(
	    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnt = contours[0]
	x, y, w, h = cv2.boundingRect(cnt)
	crop = img[y:y + h, x:x + w]
	cv2.imwrite("temp.jpg",crop)
	print(pytesseract.image_to_string(Image.open("temp.jpg")))
	os.remove("temp.jpg")