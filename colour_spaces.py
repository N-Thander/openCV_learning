"""
BGR -> is the default colour reading format of openCV
outside of openCV in other python libaries colours are usually percieved as RGB which is inverse of BGR format

secondly we cannot convert colours form Grayscale to HSV directly in openCV atleast
in order to do so we need to convert to BGR first and after that the image can be conveted to the required format


"""


import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos\park.jpg')
cv.imshow('Park', img)


"""
plt.imshow(img)
plt.show()

"""

# BGR -> Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR -> HSV(Human saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR ->  L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR -> RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)


cv.waitKey(0)
