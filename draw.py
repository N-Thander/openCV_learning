import cv2 as cv
import numpy as np


#blank to basically generate a canvas to draw on the file(image)
# 3 arguments passed lenght breadth and colour (argumets 3 as rgb)
blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank', blank)


"""

#step of drawing
# 1. paint the image a certain colour
# the colouring can br done in diffent ways by mentioning the array range

blank[:] = 0, 255, 0
cv.imshow('Green', blank)

# the colouring can br done in diffent ways by mentioning the array range
blank[200:300, 300:400] = 0,0,255
cv.imshow('redish', blank)

"""

"""

# 2. Drawing a rectangle

cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness = 2)
cv.imshow('Rectangle', blank)


# 3. Drawing a circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
cv.imshow('circle', blank)


# 4. Drawing a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('line', blank)

"""
# 5. Entering a text

cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank)


cv.waitKey(0)


#note the colour can be filled up setting the thickness == -1

"""



# image to draw on
img = cv.imread('Photos\cat.jpg')
cv.imshow('cat', img)

cv.waitKey(0)

"""
