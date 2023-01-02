import numpy as np
import cv2

class FrameOps:
  def __init__(self, img: np.array) -> None:
    self.img = img
    
    if len(self.img.shape) < 3:
      self.h, self.w = img.shape
      self.gray = self.img
    elif len(self.img.shape) == 3:
      self.h, self.w, self.d = img.shape
      self.gray = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
      self.color = self.img

  # convert gray scale image into clipped Ansel Adams zones. 0-255 -> 0.0-1.0 (clipped) -> 0-255
  def to_ansel(self) -> np.array: return np.array((np.array(np.array(((self.gray/255)*10), dtype='uint8')/10)*255), dtype='uint8')

  # run edge detection on image
  def to_edge(self, sigma: float = 0.33) -> np.array:
    m = np.median(self.gray)
    upper_threshold, lower_threshold = int(min(255, (1.0+sigma)*m)), int(max(0, (1.0-sigma)*m))
    gausian_blur = cv2.GaussianBlur(self.gray, (3, 3), cv2.BORDER_DEFAULT)
    return cv2.Canny(gausian_blur, lower_threshold, upper_threshold)

  # set gamma curve on image
  def gamma(self, sigma: float = 2.2) -> np.array:
    return np.array(255*(self.gray/255)**sigma, dtype = 'uint8')
