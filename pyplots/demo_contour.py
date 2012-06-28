import numpy as np
import pylab as pl
from scipy import ndimage

x, y = np.mgrid[0:100, 0:100]
z = np.zeros((100, 100), dtype=np.float)
z[50, 50] = 1e3
z = ndimage.gaussian_filter(z, sigma=20)

cs = pl.contour(x, y, z, 5)
pl.clabel(cs, inline=1, fontsize=10, fmt='%1.2f')
pl.show()
