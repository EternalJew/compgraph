import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt

x = np.array([1.5, 1.95, 2.4, 2.85, 3.3])
y = np.array([73, 6, 115, 48, 81])

t, c, k = interpolate.splrep(x, y, s=0, k=3)
N = 100
xmin, xmax = x.min(), x.max()
xx = np.linspace(xmin, xmax, N)
spline = interpolate.BSpline(t, c, k, extrapolate=False)

plt.plot(x, y, 'ro')
plt.plot(xx, spline(xx), 'g')
plt.grid()
plt.legend(loc='best')
plt.show()