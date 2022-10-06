#!/usr/bin/env python3

import cv2
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

face_cascade = cv2.CascadeClassifier(snap + '/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(snap + '/usr/share/opencv4/haarcascades/haarcascade_eye.xml')

def detect(gray, frame):
  """ Input = greyscale image or frame from video stream
      Output = Image with rectangle box in the face
  """
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]

    eyes = eyes_cascade.detectMultiScale(roi_gray, 1.1, 3)

    for (ex, ey, ew, eh) in eyes:
      cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)

  return frame

video_capture = cv2.VideoCapture(0)

video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cv2.namedWindow('Video',cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Video', cv2.WND_PROP_ASPECT_RATIO,
                      cv2.WINDOW_FULLSCREEN)

while True:
  ret, frame = video_capture.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  canvas = detect(gray, frame)
  cv2.imshow("Video", canvas)
  # cv2.imshow("Video", gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video_capture.release()
cv2.destroyAllWindows()
