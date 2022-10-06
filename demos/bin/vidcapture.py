#!/usr/bin/env python3

import numpy as np
import cv2
import subprocess

# force 720p as default
width = 1280
height = 720

cpuinfo = open('/proc/cpuinfo', 'r').readlines()[-1]

if 'Raspberry Pi' in cpuinfo:
  # pi is to slow for 720p, go to a lower resolution
  width = 640
  height = 360
  subprocess.run(['logger', 'On a Pi3, switching to lower resolution !'])

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cv2.namedWindow('Video',cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Video', cv2.WND_PROP_ASPECT_RATIO,
                      cv2.WINDOW_FULLSCREEN)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
