# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:10:23 2020

@author: user
"""

import cv2
import filter 

cap = cv2.VideoCapture(0)



while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    filter.detect_face(frame, block=True)
    img = filter.find_hand(frame)
    
    cv2.imshow("img",img)
    k = cv2.waitKey(5)

    if k == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
