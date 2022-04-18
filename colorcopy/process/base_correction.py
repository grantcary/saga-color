from cv2 import CAP_FFMPEG, threshold
import parse.media_parse as mp
from matplotlib import pyplot as plt
import numpy as np
import cv2
import time

image_path = 'D:/Downloads/Test Images/Photos/IMG_0597.JPG'
h, w, rgb, luma = mp.imageparse(image_path)
zones, plus_gamma, minus_gamma = mp.gamma_plus_minus(w, h, luma)
print(h, w, h*w)

m = np.median(luma)
sigma = 0.33
lower_thresh = int(max(0, (1.0-sigma)*m))
upper_thresh = int(min(255, (1.0+sigma)*m))
print(lower_thresh, upper_thresh)
# plus_gamma = plus_gamma.reshape(w, h)
luma = luma.reshape(w, h)
# plus_gamma = cv2.resize(plus_gamma, (int(h/4), int(w/4)))
# minus_gamma = cv2.resize(minus_gamma, (int(h/4), int(w/4)))
# edges = cv2.Canny(plus_gamma, lower_thresh, upper_thresh)
dup = np.unique(cv2.Canny(luma, lower_thresh, upper_thresh).flatten())
print(dup)
# plt.imshow(dup, cmap="gray")
# plt.subplot(122), plt.imshow(dup, cmap="gray")
# plt.show()


# rgb = rgb.reshape(w, h, 3)
# print(rgb.shape)
# np.flip(rgb, axis=1)
# rgb = rgb.astype(np.uint8)
# rgb = cv2.resize(rgb, (int(h/10), int(w/10)))
# winname = 'Parse'
# cv2.namedWindow(winname)
# cv2.moveWindow(winname, 40, 30)
# cv2.imshow(winname, rgb)
# cv2.waitKey(0)