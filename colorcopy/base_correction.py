from matplotlib import pyplot as plt
from cv2 import CAP_FFMPEG, threshold
import iParser as p
import numpy as np
import cv2


path = 'D:/Pictures/Family Photos/2008-2013/2012-06-15/008.JPG'
c, g, h, w = p.parse(path)
ug, lg = p.gamma(g)
a = p.ansel(g)

plt.imshow(a, cmap="gray")
plt.show()


# def canny_thresh(image, sigma=0.33):
#     m = np.median(image)
#     lower_thresh = int(max(0, (1.0-sigma)*m))
#     upper_thresh = int(min(255, (1.0+sigma)*m))
#     print(lower_thresh, upper_thresh)
#     return lower_thresh, upper_thresh

# lt, ut = canny_thresh(g)
# gblur = cv2.GaussianBlur(g, (3, 3), cv2.BORDER_DEFAULT)
# edges = cv2.Canny(gblur, lt, ut)
