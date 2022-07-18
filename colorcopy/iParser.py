import numpy as np
import cv2

def parse(dir):
  img = cv2.imread(dir)
  color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  h, w, _ = img.shape
  return color, gray, h, w

def gamma(gray):
  g_pls = np.array(255*(gray/255)**2.2, dtype = 'uint8')
  g_min = np.array(255*(gray/255)**0.455, dtype = 'uint8')
  return g_pls, g_min

def ansel(gray):
  return np.array(((gray/255)*10+0.5), dtype = 'uint8')

def edge(gray, sigma=0.33):
  m = np.median(gray)
  t_upr, t_lwr = int(min(255, (1.0+sigma)*m)), int(max(0, (1.0-sigma)*m))
  gblur = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
  return cv2.Canny(gblur, t_lwr, t_upr)
