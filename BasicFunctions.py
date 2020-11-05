import cv2
import numpy as np
img =cv2.imread('resources/lena.png')
kernal = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(9,9),0) # 0 is sigmax
imgCanny = cv2.Canny(img,150,200) #150,200 is threshold(reduce edges if increase from 100,100)
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)
imgEroded = cv2.erode(imgDialation,kernal,iterations=1)
cv2.imshow("grai image",imgGray)
cv2.imshow("blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.imshow("Erotion image",imgEroded)
cv2.waitKey(0)

