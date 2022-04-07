import cython
import cv2
import time
from PIL import Image, ImageOps
import numpy as np
cimport numpy as cnp

@cython.boundscheck(False)
cpdef rgb_to_luma(int w, int h, int[:,:] rgb_values):
    cdef cnp.ndarray luma_values
    luma_values = np.arange(w*h)
    for i in range(0, w*h):
        luma_values[i] = 0.299*rgb_values[i,0] + 0.587*rgb_values[i,1] + 0.114*rgb_values[i,2]

    return luma_values

def imageparse(image_path):
    img = ImageOps.exif_transpose(Image.open(image_path).convert('RGB'))
    w, h = img.size
    start_time = time.time()
    rgb = np.array(img.getdata())
    print(time.time()-start_time)
    start_time = time.time()
    luma = rgb_to_luma(w, h, rgb)
    print(time.time()-start_time)
    return w, h, rgb, luma