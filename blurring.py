import cv2 as cv

img = cv.imread('Photos\park.jpg')
cv.imshow('Park', img)


# Averaging 
# note the higher the kernal size the more is the blurring in the image
average = cv.blur(img, (3, 3))
cv.imshow('Average Blur', average)

# Gaussian Blur 
# it results in less blur than avg blurring tho the blurring is more natural in this form of blurring
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian Blur", gauss)

# Meadian Blur 
# used in advance computer vision for smoothing out the image
# the median blur is not usually used in large kernal size
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 3, 15, 15)
cv.imshow("Bilateral", bilateral)




cv.waitKey(0)