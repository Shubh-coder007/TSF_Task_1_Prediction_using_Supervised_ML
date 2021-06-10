
# The Sparks Foundation
# Successfully completed the Task of CV & IOT
# Author: Shubh Dholakiya
# (Data Science and Business Analytics Intern)
# Import Dependencies
import cv2
import pytesseract as pt
# Setting path
pt.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'


# Converting image to string
def ocr_core(img):
    text = pt.image_to_string(img)
    return text


# Load the image
img = cv2.imread('img.jpg')


# Get gray scale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# Thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))
