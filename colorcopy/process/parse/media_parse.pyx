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
    h, w, d = img.shape
    rgb = img.reshape(w*h, 3)
    print(time.time()-timer)
    start_time = time.time()
    luma = rgb_to_luma(h, w, rgb)
    print(time.time()-start_time)
    return w, h, rgb, luma

@cython.boundscheck(False)
cpdef gamma_plus_minus(int w, int h, int[:] luma):
    cdef np.ndarray plus_gamma = np.arange(h*w)
    cdef np.ndarray minus_gamma = np.arange(h*w)
    plus_gamma = plus_gamma.astype('uint8')
    minus_gamma = minus_gamma.astype('uint8')
    timer = time.time()
    for i in range(0, w*h):
        # zones[i] = int((luma[i]/255)*tol+0.5)/tol
        plus_gamma[i] = int(((((luma[i]/255)**(1/2.2))*255)*1.0+0.5)/1.0)
        minus_gamma[i] = int(((((luma[i]/255)**(1/0.455))*255)*1.0+0.5)/1.0)
    print(time.time()-timer)
    return plus_gamma, minus_gamma
