"""
an image histogram is a type of histogram that acts as a graphical representation of the tonal repreasntation  in a digital image.
It plots the number of 


"""

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos\cats.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel("# of pixles")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()


cv.waitKey(0)
