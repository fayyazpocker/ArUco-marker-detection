import numpy as np
import cv2
import cv2.aruco as aruco
from aruco_lib import *
import time

cap = cv2.VideoCapture(0)


det_aruco_list = {}

while (True):
	ret,frame = cap.read()
	det_aruco_list = detect_Aruco(frame)
	if(det_aruco_list):
		img = mark_Aruco(frame,det_aruco_list)
		robot_state = calculate_Robot_State(img,det_aruco_list)
		
	cv2.imshow('image',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
