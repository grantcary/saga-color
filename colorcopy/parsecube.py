from re import I
import numpy as np
import time

lut = 'C:/ProgramData/Blackmagic Design/DaVinci Resolve/Support/LUT/WIR Dolce LUT Collection/WIR Dolce 01.cube'

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
  return cubeSize, np.array(list(map(lambda y: y[:-2].split(), (i for i in cubeLines)))).astype(float)

def cube2lut(path):
  cubeSize, cubeValues = parsecube(path)
  lattice = np.zeros((cubeSize, cubeSize, cubeSize))

  for i, values in enumerate(cubeValues):
    rIndx, gIndx, bIndx = i%cubeSize, ((i%(cubeSize*cubeSize))/(cubeSize)), i/(cubeSize*cubeSize)
