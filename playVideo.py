
import sys
import os

os.system('export PYTHONPATH="/usr/local/lib/python2.7/site-packages:$PYTHONPATH"')

import cv2
import numpy as np


fileNamePath = "/Users/Arvi/simple_test_flask2/templates/phonemes/"

cap = cv2.VideoCapture(fileName)
while(cap.isOpened()):
  ret,frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame', gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

