# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:19:07 2021

@author: jiju4
"""


import imageio as iio
import matplotlib.pyplot as plt

camera = iio.get_reader("<video0>")
screenshot = camera.get_data(0)
camera.close()

plt.imshow("X")

import PyCapture2
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

bus = PyCapture2.BusManager()
numCams = bus.getNumOfCameras()
camera = PyCapture2.Camera()
uid = bus.getCameraFromIndex(0)
camera.connect(uid)
camera.startCapture()

while True:
    image = camera.retrieveBuffer()
    row_bytes = float(len(image.getData())) / float(image.getRows());
    cv_image = np.array(image.getData(), dtype="uint8").reshape((image.getRows(), image.getCols()) );
    cv2.imshow('frame',cv_image)
    cv2.waitKey(10)
    
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()