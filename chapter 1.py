import cv2
# READ IMAGES,VIDEO AND WEBCAM

# read image
img1 = cv2.imread('./resources/lena.png')
cv2.imshow('output',img1)
cv2.waitKey(0)

# read video
cap = cv2.VideoCapture("resources/test_video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

#  read webcam
cap = cv2.VideoCapture(0)
cap.set(3,640) # width
cap.set(4,480) # height
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

