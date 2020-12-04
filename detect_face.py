import cv2

import matplotlib.pyplot as plt
import time


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0,0))
cv2.imshow('img', img)
cv2.waitKey()



# def convertToRGB(img):
#     return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# test1 = cv2.imread('test.jpg')
# gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
# plt.imshow(gray_img, cmap='gray')


# haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
# faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

# # cv2.imshow('Test Imag', gray_img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# print('Faces found: ', len(faces))


# plt.imshow(convertToRGB(test1))   