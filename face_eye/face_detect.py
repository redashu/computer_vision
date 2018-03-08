#!/usr/bin/python3

import  cv2
import numpy as np
fc=cv2.CascadeClassifier()
fc.load('haarcascade_frontalcatface.xml')
eye_cascade=fc.load('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)

while True:
	ret,img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	f=fc.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in f:
		cv2.ractangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray=gray[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]
	cv2.imshow('windwos',img)
	if cv2.waitKey(30) & 0xFF == ord('q') :
		break

cap.release()
cv2.destroyAllWindows()
	
