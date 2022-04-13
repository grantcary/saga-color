#cython: language_level=3
import cython
import cv2
import time
import numpy as np
cimport numpy as np

@cython.boundscheck(False)
cpdef rgb_to_luma(int w, int h, unsigned char[:,:] rgb_values):
    cdef np.ndarray luma_values = np.arange(w*h)
    for i in range(0, w*h):
            luma_values[i] = 0.299*rgb_values[i, 0] + 0.587*rgb_values[i, 1] + 0.114*rgb_values[i, 2]
    return luma_values

def imageparse(image_path):
    timer = time.time()
    img = cv2.imread(image_path)
    w, h, d = img.shape
    rgb = img.reshape(w*h, 3)
    print(time.time()-timer)
    start_time = time.time()
    luma = rgb_to_luma(w, h, rgb)
    print(time.time()-start_time)
    return w, h, rgb, luma

@cython.boundscheck(False)
cpdef luma_zones(int w, int h, int[:] luma):
    cdef np.ndarray zones = np.arange(w*h)
    zones = zones.astype('float')
    timer = time.time()
    for i in range(0, w*h):
        tol = float(10**1)
        zones[i] = int((luma[i]/255)*tol+0.5)/tol
    print(time.time()-timer)
    return zones
