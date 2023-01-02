from imageparser import FrameOps
import numpy as np
import cv2

path = '/home/grant/Desktop/compute.jpg'

img = cv2.imread(path)

x = FrameOps(img)
a, b = x.gamma(2.2), x.gamma(0.455)
z = x.gray

cv2.imshow('image', z)
cv2.waitKey(0)
