# skal være ett eksempel på konturer men fungerer ikke foreløpig.

import numpy as np
import cv2 as cv

img = cv.imread('img.bmp')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 50, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cnt = contours[4]
new_img = cv.drawContours(img, [cnt], 0, (0,255,0), 3)

cv.imwrite("new.jpg", new_img)

