import cv2 as cv

"""
#reading image
img = cv.imread('Photos\cat_large.jpg')
cv.imshow('Cat', img)
# basically waits for a key to be entered tho for input '0' the key waits for an infinte amt of time
cv.waitKey(0)

"""


# reading video files
# NOTE VIDEO CAPTURE (ARGUMENT) -> REFERS TO THE CAMERA NUMBER normally it is cam 0 for webcam and ...... here simpy the path
capture = cv.VideoCapture('Videos\dog.mp4')

# using loop to read the file frame by frame

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


