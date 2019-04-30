from pylab import *
from numpy import NaN

figure(figsize = (10, 10))

def m(a):
    z = 0
    for n in range(1, 100):
        z = z**2 + a
        if abs(z) > 2:
            return n
    return NaN

X = arange(-2, .8, .001)
Y = arange(-1.5,  1.5, .001)
Z = zeros((len(Y), len(X)))

for iy, y in enumerate(Y):
    #print (iy, "of", len(Y))
    for ix, x in enumerate(X):
        Z[iy,ix] = m(x + 1j * y)

imshow(Z, cmap = plt.cm.inferno, extent = (X.min(), X.max(), Y.min(), Y.max()))
xlabel("Re(c)")
ylabel("Im(c)")

show()