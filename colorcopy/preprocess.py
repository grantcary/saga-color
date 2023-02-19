import os
from os.path import expanduser
from frame import FrameOps, Image
from matplotlib import pyplot as plt

DATASET = f'{expanduser("~")}/Desktop/dataset'
TEST_IMAGE = f'{expanduser("~")}/Desktop/Images/testimage.jpg'

plt.imshow(Image(TEST_IMAGE).rotate_and_scale(angle=20, scale=2), cmap='gray')
plt.show()

print(os.listdir(DATASET))