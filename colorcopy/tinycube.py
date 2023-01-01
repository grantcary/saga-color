from matplotlib import pyplot as plt
from time import time
import numpy as np
import itertools

import colorcopy.imageparser as parse

# Resources
# https://github.com/colour-science/colour
# https://developer.nvidia.com/gpugems/gpugems2/part-iii-high-quality-rendering/chapter-24-using-lookup-tables-accelerate-color

# A lot of code snippets from Thomas Mansencal's Colour Science library were used to make this current version work
# on average about 0.2 seconds faster than Thomas' implementation, but WAY less flexible

# LUT Readout Example:
# Dimensions: 3
# Domain: [[ 0.  0.  0.]
#          [ 1.  1.  1.]]
# Size: 32

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

def prepimage(RGB): return tstack(tsplit(RGB/255).astype('float32'))
# tstack([((j-domainMin[i])/(domainMax[i]-domainMin[i]))*(1-0)+0 for i, j in enumerate((R, G, B))])/255

def parsecube(path):
  cubeFile = open(path, newline='')
  cubeFileLines = cubeFile.readlines()
  cubeFile.close()

  # get/find cube dimensions and cube value lines only
  size_index = 0
  size = -1
  for i, line in enumerate(cubeFileLines):
    if "LUT_3D_SIZE" in line:
      size = int(line.split()[1])
    if len(line) > 0 and len(line.split()) == 3 and "#" not in line:
      size_index = i
      break

  # if not defined in cube file parse (DOMIN_MIN, DOMAIN_MAX), use these values
  domainMin, domainMax = np.array([0, 0, 0]), np.array([1, 1, 1])
  domain = np.vstack([domainMin, domainMax]).astype('float32')
  
  # creates 3D lookup table from raw cube file floats
  raw_data = cubeFileLines[size_index:size_index+(size**3)]
  data = np.array(list(map(lambda y: y[:-2].split(), (i for i in raw_data))), dtype='float32')
  table = data.reshape([size, size, size, 3], order='F')

  return domain, table

def vertcoords(V_xyz, table):
  V_xyz = np.reshape(np.clip(V_xyz, 0, 1), (-1, 3))
  i_m = np.array(table.shape[0:-1]) - 1
  i_f = np.floor(V_xyz * i_m).astype(int)
  i_c = np.clip(i_f + 1, 0, i_m)
  V_xyzr = i_m * V_xyz - i_f
  i_f_c = i_f, i_c
  print(i_f_c)

  # itertools.product(*zip([0, 0, 0], [1, 1, 1]))
  # output test corners
  #   (0.0, 0.0, 0.0),
  #   (1.0, 0.0, 0.0),
  #   (0.0, 1.0, 0.0),
  #   (1.0, 1.0, 0.0),
  #   (0.0, 0.0, 1.0),
  #   (1.0, 0.0, 1.0),
  #   (0.0, 1.0, 1.0),
  #   (1.0, 1.0, 1.0)

  vertices = np.array([table[i_f_c[i[0]][..., 0], i_f_c[i[1]][..., 1], i_f_c[i[2]][..., 2]] for i in itertools.product(*zip([0, 0, 0], [1, 1, 1]))])
  return vertices, V_xyzr

@timer
def lutapplication(RGB, table):
  RGB = prepimage(RGB)
  vertices, V_xyzr = vertcoords(RGB, table)

  vertices = np.moveaxis(vertices, 0, 1)
  x, y, z = (f[:, np.newaxis] for f in tsplit(V_xyzr))

  weights = np.moveaxis(np.transpose([(1 - x) * (1 - y) * (1 - z),
                                      (1 - x) * (1 - y) * z,
                                      (1 - x) * y * (1 - z),
                                      (1 - x) * y * z,
                                      x * (1 - y) * (1 - z),
                                      x * (1 - y) * z,
                                      x * y * (1 - z),
                                      x * y * z]), 0, -1)

  return np.reshape(np.sum(vertices * weights, 1), RGB.shape)


domain, table = parsecube(lut)
new_img = (lutapplication(color, table)*255).astype('uint8')

plt.imshow(new_img)
plt.show()

# d, t = parsecube(lut)
# c = prepimage(color, d[0], d[1])
# v, _ = vandrc(c, t)