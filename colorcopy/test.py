from frame import Image, FrameOps
import imutils
import PIL.Image
import numpy as np
from matplotlib import pyplot as plt
from os.path import expanduser

DATASET = f'{expanduser("~")}/Desktop/Images/testimage.jpg'

def side_by_side(imgs: np.array):
    _, plot = plt.subplots(1, len(imgs))
    for i, img in enumerate(imgs):
      if len(img.shape) == 3:
        plot[i].imshow(img)
      elif len(img.shape) < 3: 
        plot[i].imshow(img, cmap='gray')
    plt.show()

img_0 = Image(DATASET).img
img_1 = Image(DATASET).gamma_curve(0.455)

side_by_side([img_0, img_1])