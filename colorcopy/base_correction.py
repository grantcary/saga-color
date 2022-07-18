from matplotlib import pyplot as plt
import iParser as parse

path = 'D:/Pictures/Family Photos/2008-2013/2012-06-15/008.JPG'


c, g, h, w = parse.parse(path)
u, l = parse.gamma(g)
a = parse.ansel(g)
e = parse.edge(g)

plt.imshow(e, cmap='gray')
plt.show()