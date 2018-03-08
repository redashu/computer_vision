#!/usr/bin/python3
import  cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap=cv2.VideoCapture(0)
while True:
	status,img=cap.read()
	grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(grayimg,1.15,5)  
	for  (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
		roi_gray=grayimg[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]
		eyes=eye_cascade.detectMultiScale(roi_gray,1.15,5)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(200,120,30),4)  
			
	cv2.imshow('imgw',img)
	k=cv2.waitKey(30) & 0xff
	if k == 27:
		break		
cap.release()
cv2.destroyallWindows()

"""
cv2.imshow('gray',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
