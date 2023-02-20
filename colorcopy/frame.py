from scipy import ndimage
import numpy as np
import imutils
import cv2

class FrameOps:
  def __init__(self, img: np.array) -> None:
    self.img = img

  @property
  def gray(self) -> np.array:
    return cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)

  def resize(self, size: tuple[int, int]) -> np.array:
    return cv2.resize(self.img, dsize=size)

  def crop(self, x: int, y: int, w: int, h: int) -> np.array:
    return self.img[y:y+h, x:x+w]
  
  def rotate_and_scale(self, angle: int = 0, center: tuple[int, int] = None, scale: float = 1.0) -> np.array:
    return imutils.roatate(angle, center, scale)

  def rotate_bound(self, angle: int) -> np.array:
    return imutils.rotate_bound(self.img, angle)
  
  def flip(self, axis: int = 0) -> np.array:
    return cv2.flip(self.img, axis)
  
  def normalize(self, min, max) -> np.array:
    return cv2.normalize(self.img, None, min, max, cv2.NORM_MINMAX)
  
  def gamma_curve(self, sigma: float = 2.2) -> np.array:
    return np.array(255*(self.img/255)**sigma, dtype = 'uint8')
  
  # convert gray scale image into clipped Ansel Adams zones. 0-255 -> 0.0-1.0 (clipped) -> 0-255
  @property
  def ansel(self) -> np.array:
    image = self.img
    if len(image.shape) == 3:
      image = self.gray
    return np.array((np.array(np.array(((image/255)*10), dtype='uint8')/10)*255), dtype='uint8')

  def canny(self, sigma: float = 0.9) -> np.array:
    image = self.img
    if len(image.shape) == 3:
      image = self.gray
    gausian_blur = ndimage.gaussian_filter(image, sigma=sigma)
    return imutils.auto_canny(gausian_blur)

class Image(FrameOps):
  def __init__(self, path: str) -> None:
    img = cv2.imread(path)
    
    if len(img.shape) < 3:
      self.img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif len(img.shape) == 3:
      self.img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)