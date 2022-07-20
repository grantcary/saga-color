from matplotlib import pyplot as plt
import iParser as parse
import numpy as np
from time import time

# Resources
# https://developer.nvidia.com/gpugems/gpugems2/part-iii-high-quality-rendering/chapter-24-using-lookup-tables-accelerate-color


img = 'D:/Pictures/Family Photos/2008-2013/2012-06-15/008.JPG'
lut = 'C:/ProgramData/Blackmagic Design/DaVinci Resolve/Support/LUT/WIR Dolce LUT Collection/WIR Dolce 01.cube'

color, _, h, w = parse.parse(img)

def timer(func):
  def wrapper(*args, **kwargs):
    st = time()
    result = func(*args, **kwargs)
    print(f'Function {func.__name__!r} executed in {(time()-st):.4f}s')
    return result
  return wrapper

def tstack(RGBchans : list): return np.concatenate([x[..., np.newaxis] for x in RGBchans], axis=-1)
def tsplit(cubeValues): return np.array([cubeValues[..., x] for x in range(cubeValues.shape[-1])])
def linear_interpolation(): pass

def parsecube(path):
  cubeFile = open(path, newline='')
  cubeFileLines = cubeFile.readlines()
  cubeFile.close()

  # get/find cube dimensions and cube value lines
  size_index = 0
  cubeSize = -1
  for i, line in enumerate(cubeFileLines):
    if "LUT_3D_SIZE" in line:
      cubeSize = int(line.split()[1])
    if len(line) > 0 and len(line.split()) == 3 and "#" not in line:
      size_index = i
      break

  cubeLines = cubeFileLines[size_index:size_index+(cubeSize**3)]

  # This next line is wrong. LUT mapping doesn't work properly. Do correctly.
  # Maybe use upper and lower uint8 bounds to calculate lut table mapping beforehand
  return tsplit(np.array(list(map(lambda y: y[:-2].split(), (i for i in cubeLines))), dtype='float')*255)

@timer
def cube2lut(path, image, h, w):
  # assign parsecube() to variables outside of this function to save runtime
  x, y, z = parsecube(path)
  r, g, b = tsplit(np.reshape(image , (h*w, 3)))

  # not entirely sure if x, y, z maps to r, g, b sequentially 
  r, g, b = x[r], y[g], z[b]
  
  return np.reshape(tstack([(r).astype(np.uint8), (g).astype(np.uint8), (b).astype(np.uint8)]), (h, w, 3))

new_img = cube2lut(lut, color, h, w)

plt.imshow(new_img)
plt.show()
