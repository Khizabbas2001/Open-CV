
import cv2
import pytesseract
def ocr_core(xyz):
    text = pytesseract.image_to_string(xyz)
    return text
image = cv2.imread('xyz.png')


# grayscale

def get_greyscale(image):
 return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise remove

def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


#test = get_greyscale(test)
#test = thresholding(test)
test = remove_noise(image)

print(ocr_core(image))