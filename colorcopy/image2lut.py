from matplotlib import pyplot as plt
import colorcopy.imageparser as parse
import numpy as np
import colour
import time

img = 'D:/Pictures/Family Photos/2008-2013/2012-06-15/008.JPG'
# Test LUT
lut = 'C:/ProgramData/Blackmagic Design/DaVinci Resolve/Support/LUT/WIR Dolce LUT Collection/WIR Dolce 05.cube'

c, _, _, _ = parse.parse(img)


def lut_instance(lut): return colour.read_LUT(lut)
def apply_lut(img, lut): return (lut.apply(img.astype(np.float32)/255)*255).astype(np.uint8)

x = lut_instance(lut)
st = time.time()
y = apply_lut(c, x)
print(time.time()-st)
# plt.imshow(apply_lut(c, lut_instance(lut)))
# plt.show()
