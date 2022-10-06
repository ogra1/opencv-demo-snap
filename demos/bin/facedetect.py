#!/usr/bin/env python3

import cv2
import sys
import os
import subprocess

snap = os.environ["SNAP"]

# force 720p as default
width = 1280
height = 720

cpuinfo = open('/proc/cpuinfo', 'r').readlines()[-1]

if 'Raspberry Pi' in cpuinfo:
  # pi is to slow for 720p, go to a lower resolution
  width = 640
  height = 360
  subprocess.run(['logger', 'On a Pi3, switching to lower resolution !'])


cascPath = snap + "/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cv2.namedWindow('Video',cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Video', cv2.WND_PROP_ASPECT_RATIO,
                      cv2.WINDOW_FULLSCREEN)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
