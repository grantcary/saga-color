import numpy as np
import cv2

def parse(dir):
    img = cv2.imread(dir)
    color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w, _ = img.shape
    return color, gray, h, w

def gamma(gray):
    g_pls = np.array(255*(gray/255)**0.455, dtype = 'uint8')
    g_min = np.array(255*(gray/255)**2.2, dtype = 'uint8')
    return g_pls, g_min

def ansel(gray):
    zones = np.array(((gray/255)*10+0.5)/10, dtype = 'uint8')
    return zones