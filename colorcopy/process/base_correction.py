import parse.media_parse as mp
import numpy as np
import cv2
import time

image_path = 'D:/Downloads/Test Images/Photos/facetest.jpg'
w, h, rgb, luma = mp.imageparse(image_path)
zones = mp.luma_zones(w, h, luma)
print(w, h)
print(rgb, len(rgb))
print(luma, len(luma))

rgb = rgb.reshape(w, h, 3)
print(rgb.shape)
np.flip(rgb, axis=1)
rgb = rgb.astype(np.uint8)
rgb = cv2.resize(rgb, (495, 742))
cv2.imshow('image', rgb)
cv2.waitKey(0)