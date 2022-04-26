from cv2 import CAP_FFMPEG, threshold
import parse.media_parse as mp
from matplotlib import pyplot as plt
import numpy as np
import cv2
import time

image_path = 'D:/Downloads/Test Images/Photos/test/frontal.jpg'
h, w, rgb, luma = mp.imageparse(image_path)
zones, plus_gamma, minus_gamma = mp.gamma_plus_minus(w, h, luma)
print(h, w, h*w)

def canny_thresh(image, sigma=0.33):
    m = np.median(image)
    lower_thresh = int(max(0, (1.0-sigma)*m))
    upper_thresh = int(min(255, (1.0+sigma)*m))
    print(lower_thresh, upper_thresh)
    return lower_thresh, upper_thresh


def tester(w, h, image_set, x=False):
    lower_thresh, upper_thresh = canny_thresh(image_set[0])
    
    edge_set = []
    for i, image in enumerate(image_set):
            img = image.reshape(w, h)
            image_set[i] = img
            gblur = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
            edges = cv2.Canny(gblur, lower_thresh, upper_thresh)
            edge_set.append(edges)

    if x:
        a, b, c = edge_set
        s = sum(sum(a))+sum(sum(b))+sum(sum(c))
        print("high: ", sum(sum(b))/s, " low: ", sum(sum(c))/s)
        for i in range(len(image_set)):
            plt.subplot(121), plt.imshow(image_set[i], cmap="gray")
            plt.subplot(122), plt.imshow(edge_set[i], cmap="gray")
            plt.show()
    else:
        for i in range(len(edge_set)-1):
            plt.subplot(121), plt.imshow(edge_set[i], cmap="gray")
            plt.subplot(122), plt.imshow(edge_set[i+1], cmap="gray")
            plt.show()

tester(w, h, [luma, plus_gamma, minus_gamma], True)

# print(np.sum(can)/255, np.sum(can2)/255, np.sum(merged)/255)
