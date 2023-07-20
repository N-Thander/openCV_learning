"""
conturs are basically the line forming the boundary of an object and may seem like an edge tho mathematically they are different

--> difference form stack overflow

Edges are computed as points that are extrema of the image gradient in the direction of the gradient. if it helps,
you can think of them as the min and max points in a 1D function. 
The point is, edge pixels are a local notion: they just point out a significant difference between neighbouring pixels.

Contours are often obtained from edges, but they are aimed at being object contours. Thus, they need to be closed curves.
You can think of them as boundaries (some Image Processing algorithms & librarires call them like that).
When they are obtained from edges, you need to connect the edges in order to obtain a closed contour.

"""

"""
in general we can get away by treating contours as edges 

secondly: while finding contours it is better to apply canny's method than using threshold and CHAIN_APPROX_SIMPLE method



"""



import cv2 as cv
import numpy as np

img = cv.imread('Photos\cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)



#conversion to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

"""
blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#finding edges(canny method used)
canny = cv.Canny(blur, 125, 175)
cv.imshow("canny", canny)

"""

# alternative method with threshold
# threshold can be comsidered as a form of makinga a binary form of an image there it is either black or white

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)


#finding contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# drawing the contours:
# -1 -> we are drawing all the points
# (0, 0, 255) -> BGR colour format
# 2 -> thickness
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours Drawn", blank)



cv.waitKey(0)