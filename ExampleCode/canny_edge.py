import io
import cv2
import numpy as np
import time
from collections import defaultdict
from picamera import PiCamera
from picamera.array import PiRGBArray

camera = PiCamera()

#lager bildet til HSL farger
def to_hsl(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

#isolerer hvit fra HSL
def isolate_white_hsl(img):
    low = np.array([0,200,0], dtype=np.uint8)
    high = np.array([180,255,255], dtype=np.uint8)

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

rest = 0

resolution_width = 640
resolution_hight = 480

turn_margin = 40

camera.resolution = (resolution_width, resolution_hight)
camera.framerate = 10
#camera.crop(0.25, 0.25, 0.75, 0.75)
rawCapture = PiRGBArray(camera, size=(resolution_width, resolution_hight))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array
    #cv2.imwrite("RAW.jpg",image)

    new_img = filter_img(image)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    #ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

    mask = cv2.erode(blur, None, iterations=2)

    mask = cv2.dilate(mask, None, iterations=2)

    #mask = cv2.bitwise_not(mask)

    contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)[-2:]

#final_img = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

#cv2.line(final_img,(cx,0),(cx,resolution_hight),(255,0,0),1)
#cv2.line(final_img,(0,cy),(resolution_width,cy),(255,0,0),1)
#cv2.drawContours(final_img, contours, -1, (0,255,0), 1)

#cv2.imwrite("mask.jpg", mask)

#cv2.imwrite("final.jpg", final_img)

