import parse.media_parse as mp
from matplotlib import pyplot as plt
import numpy as np
import cv2
import time

image_path = 'D:/Downloads/Test Images/Photos/facetest.jpg'
h, w, rgb, luma = mp.imageparse(image_path)
plus_gamma, minus_gamma = mp.gamma_plus_minus(w, h, luma)
print(h, w, h*w)
print(rgb, len(rgb))
print(luma, len(luma))
print(plus_gamma, len(plus_gamma))
print(minus_gamma, len(minus_gamma))

# minus_gamma = minus_gamma.reshape(w, h)
# plt.imshow(minus_gamma, cmap="gray")
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