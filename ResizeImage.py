import cv2
import numpy as np
img = cv2.imread('resources/lambo.png')
print(img.shape)

imgCropped = img[:200,200:500]  #height,width

imgResize = cv2.resize(img,(300,200)) # width,height
cv2.imshow('image',img)
cv2.imshow('resize img',imgResize)
cv2.imshow('cropped img',imgCropped)
cv2.waitKey(0)


# Draw shapes on images
img = np.zeros((512,512,3),np.uint8) #(hight,width)

img[:]= 255,0,0
cv2.line(img,(0,0),(212,400),(0,255,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #(width,height)
#(0,0)starting point of line,(300,300) end poitn of line,color of line,3 is the thickness
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) #fill color
cv2.circle(img,(400,50),30,(255,255,0),5) #center,radius,color,thickness
cv2.putText(img,"opencv",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
# (image,text,origin where text is required,font of the text,scale(size of the text),color,thickness)
cv2.imshow('image',img)
cv2.waitKey(0)