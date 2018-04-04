import numpy as np
import cv2
import cv2.aruco as aruco
from aruco_lib import *
import time

cap = cv2.VideoCapture(0)


det_aruco_list = {}
last_time=0

while (True):
	ret,frame = cap.read()
	#print frame.shape
	det_aruco_list = detect_Aruco(frame)
	cur_time = int(round(time.time() * 1000))
	if(det_aruco_list):

		img = mark_Aruco(frame,det_aruco_list)
		robot_state = calculate_Robot_State(img,det_aruco_list)
		#print robot_state
		#print min(robot_state.keys()), robot_state[(min(robot_state.keys()))]
		#cv2.circle(img,(255,50),1,(0,0,255),2)
		#print cur_time - last_time
		last_time = cur_time
	cv2.imshow('image',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()