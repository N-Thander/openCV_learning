import cv2 as cv
import numpy as np

img = cv.imread('Photos\park.jpg')
cv.imshow("Park", img)

# 1. Translation : shifting the image along the diffetnt axis

def translate(img, x, y):
    #tranlation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


"""
-x --> Left
-y --> Up
x --> Right
y --> Down

"""
    
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)


# 2. Rotation

def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

"""
-ve -> angle for clockwise
+ve -> angle for anti-clockwise transformation

"""

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)



# 3. Resizing 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# 4. Fliping
"""
0 -> vertically
1 -> horizontally
-1 -> both vertically and horizontally

"""
flip = cv.flip(img, 0)

cv.waitKey(0)