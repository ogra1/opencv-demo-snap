#!/usr/bin/env python3

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

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
