import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('Photos\cats.jpg')
cv.imshow('cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('mask', mask)

# colour histogram
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('no. of pixels')
colours = ('b', 'g', 'r')
# enumerate is bulid in functionin python that allows one to keep track of the number of iterations(loops) in a loop
for i, col in enumerate(colours):
    hist = cv.calcHist([img], [i], None, [256], [0, 265])
    plt.plot(hist, colours = col)
    plt.xlim([0, 256])





plt.show()
cv.waitKey(0)
