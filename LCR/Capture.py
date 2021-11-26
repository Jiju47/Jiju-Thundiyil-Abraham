# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:28:01 2021

@author: jiju4
"""

from __future__ import print_function
import numpy as np
import cv2

# detect all connected webcams
valid_cams = []
for i in range(8):
    cap = cv2.VideoCapture(i)
    if cap is None or not cap.isOpened():
        print('Warning: unable to open video source: ', i)
    else:
        valid_cams.append(i)

caps = []
for webcam in valid_cams:
    caps.append(cv2.VideoCapture(webcam))

while True:
    # Capture frame-by-frame
    for webcam in valid_cams:
        ret, frame = caps[webcam].read()
        # Display the resulting framefrom cv2 import cv2
        cv2.imshow('webcam'+str(webcam), frame)
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break

# When everything done, release the capture
for cap in caps:
    cap.release()

cv2.destroyAllWindows()


