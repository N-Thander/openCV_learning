import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    #note this method works with images, videos and live videos also
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # works only with live videos exclusively like web cam 
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('Videos\dog.mp4')

while True:
    
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF ==ord('d'):
        break




"""
img = cv.imread('Photos\cat_large.jpg')
resised_image = rescaleFrame(img)
cv.imshow('Image', resised_image)

"""

cv.waitKey(0)