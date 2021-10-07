import cv2
import numpy as np

def to_hsl(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

#isolerer hvit fra HSL
def isolate_white_hsl(img):
    low = np.array([0,200,0], dtype=np.uint8)
    high = np.array([190,255,255], dtype=np.uint8)

    white_mask = cv2.inRange(img, low, high)

    return white_mask

#setter sammen orginal og hvitt bilde
def merge_white_original(img, hsl_white):

    return cv2.bitwise_and(img,img,mask=hsl_white)

#legger sammen bildene
def filter_img(img):
    hsl_img = to_hsl(img)
    hsl_white = isolate_white_hsl(hsl_img)

    return merge_white_original(img, hsl_white)

image = cv2.imread("img.jpg")

new_img = filter_img(image)
gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

#ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

mask = cv2.erode(blur, None, iterations=2)

mask = cv2.dilate(mask, None, iterations=2)

#mask = cv2.bitwise_not(mask)

#contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)[-2:]

cv2.imwrite("new.jpg", new_img)

