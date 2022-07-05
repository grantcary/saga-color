from matplotlib import pyplot as plt
import iParser as p
import numpy as np
import cv2

path = 'D:/Pictures/Family Photos/2008-2013/2012-06-15/008.JPG'


c, g, h, w = p.parse(path)
u, l = p.gamma(g)
a = p.ansel(g)
e = p.edge(g)

plt.imshow(e, cmap='gray')
plt.show()
