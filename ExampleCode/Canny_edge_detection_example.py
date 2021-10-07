#lett test av canny edge detection.

import cv2
import numpy as np

img = cv2.imread('img.bmp',0)
edges = cv2.Canny(img,100,120)

cv2.imwrite("new.jpg", edges)