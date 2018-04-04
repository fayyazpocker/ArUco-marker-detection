import numpy as np
import cv2
import cv2.aruco as aruco
 
 
'''
    drawMarker(...)
        drawMarker(dictionary, id, sidePixels[, img[, borderBits]]) -> img
'''
 
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_1000) #creating aruco dictionary...250 markers and a marker size of 6x6 bits
print(aruco_dict)
# second parameter is id number
# last parameter is total image size
img = aruco.drawMarker(aruco_dict, 650, 400) # 2-- marker id, as the chose dictionary is upto 250...so the id no ranges from 0 to 249....and 700x700 is the pixel size
print img.shape
cv2.imwrite("Aruco_ids/test_marker11_big.jpg", img)
print img.shape
cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()