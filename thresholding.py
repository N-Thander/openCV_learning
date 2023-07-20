"""
Image thresholding is a simple and effective way of partitioning an image into a foreground and background
This image into forground and background. The image analysis techique is a type of image segementation that isolates objects by converting 
grayscale image into binary image. Image thresholding is most effective in images with high level of contrast

"""

import cv2 as cv

img = cv.imread('Photos\cats.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grascale", gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)

# simple thresholding inverse
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inverse", thresh_inv)

# Adaptive Thresholding 
# the value here 11 is block value aka the mean about which the threshold is calculated while 3 is a constant used for fine tuning
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adapticve Threshold", adaptive_thresh)





cv.waitKey(0)