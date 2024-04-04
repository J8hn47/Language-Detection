import cv2
import imutils
import pytesseract
from PIL import Image

####### Clean up picture and resize to allow for better reading #######

# Load image, enlarge, convert to grayscale, Otsu's threshold
image = cv2.imread('C:\\Users\\c261941\\Downloads\\Grid Form.png')
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Remove horizontal
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,1))
detect_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(image, [c], -1, (255,255,255), 5)

# Remove vertical
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,25))
detect_vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
cnts = cv2.findContours(detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(image, [c], -1, (255,255,255), 5)

cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.waitKey()

########################### Read image ###########################

# # Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\c261941\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

# Open an image file
image = Image.open('C:\\Users\\c261941\\Downloads\\Grid Form.png')

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
