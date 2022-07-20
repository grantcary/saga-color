import numpy as np

lut = np.array([0, 10, 20, 30, 40])
target = np.array([2, 2, 4, 1, 3, 0, 4, 3, 1])
print(lut[target])

a = np.array([[0, 0, 0], 
              [1, 1, 1], 
              [2, 2, 2], 
              [3, 3, 3]], dtype='float')

b = np.copy(a)

x, y, z = np.array([a[..., x] for x in range(3)])
m, n, o = np.array([np.flip(b)[..., x] for x in range(3)])
print(x, m)
print(np.array((x*m)))



# size_array = np.tile(3, 3)
# for i, a in enumerate([x, y, z]):
#   samples = np.linspace(a[0], a[1], size_array[i])
#   print(samples)