"""
Gradients:  are in priciple 2D derivatives. So first the gradient itself is a real functionin the size of the image which may have 
low or high values, depending on the derivative at each point .

Edges on the other hand, are considered to be binary indicator(per pixel) of whether an edge is present

"""


import cv2 as cv
import numpy as np

img = cv.imread('Photos\cats.jpg')
cv.imshow('cats', img)

# conversion to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
soblex = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobley = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("Sobel X", soblex)
cv.imshow("Sobel Y", sobley)

combined_Sobel = cv.bitwise_or(soblex, sobley)
cv.imshow('combined_soble', combined_Sobel)


# Canny 
# note canny is a more advanc from of sobel and being a multi-step process it is uses sobel in some intermediate stage 
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)