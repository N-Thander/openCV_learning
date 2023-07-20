"""
masking: masking is an img processing method in which we define a small 'image piece' and use it to modify a larger image 

masking is as image process that is underneath many types of image processing. Including edge detection, motion detection, and noise reduction.

"""


import cv2 as cv
import numpy as np

img = cv.imread('Photos\cats.jpg')
cv.imshow('cats', img)

# note data size of masking must be equal to the dimensions of the original image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank_canvas", blank)

# masking
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked", masked)


cv.waitKey(0)
