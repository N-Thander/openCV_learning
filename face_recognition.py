import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

DIR = r'D:\Open CV\Faces\train'
people = []
for i in os.listdir(DIR):
    people.append(i)

#features = np.load('features.npy')
#labels = np.load('lables.npy')


face_reacognizer = cv.face.LBPHFaceRecognizer_create()
face_reacognizer.read('face_trained.yml')

img = cv.imread(r'Faces\val\ben_afflek\2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#Detect the face in the image
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in face_rect:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_reacognizer.predict(face_roi)
    print(f'Label = {people[label]} with condfidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)