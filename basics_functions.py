# note through out all of learning process the images used are in BGR format
import cv2 as cv

img = cv.imread('Photos\park.jpg')
cv.imshow('park', img)

# 1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur an image: basically removes some of the noise form the image
# the (3, 3) in the code represents ksize of kernal size and it must be odd numbers 
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


# 3. Edge Cascade -> finding the edges present in the image here used the canny edge detection
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# 4. Dialating the image -> dialating the image is done base on the edges; here the edges used the above canny edge
dialated = cv.dilate(canny, (3, 3), iterations= 3)
cv.imshow('Dialated', dialated)

# 5. Eroding -> basically the opposite of dialation
eroded = cv.erode(dialated, (3, 3,), iterations=3)
cv.imshow("eroded", eroded)

# 6. Resize -> resizes the image ignoring the aspect ratio
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resize", resized)

"""
note
INTER_AREA -> if reducing/shrinking the size of the image
INTER_LINEAR -> to upscale the size of the image
INTER_CUBIC -> it is also for upscaleing the size of the image how ever it produces a much higher quality image

"""
# cropping -> since images are basically a array matix cropping is done by array slicing
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)


cv.waitKey(0)