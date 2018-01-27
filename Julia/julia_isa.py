# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:24:26 2018

@author: Usuario
"""

import matplotlib.pyplot as plt
import numpy as np
import numba

# Building the Julia set
def py_julia_fractal(z_re, z_im, j, c):
    for m in range(len(z_re)):
        for n in range(len(z_im)):
		    # assigning the initial value to z
            z = z_re[m] + 1j * z_im[n]
            for t in range(256):
			    # defining the mathematical function
                z = z ** 2 + c
				# the number comes out of the set
                if np.abs(z) > 2.0:
                    j[m, n] = t
                    break

# compiling the function                    
jit_julia_fractal = numba.jit(nopython=True)(py_julia_fractal)

# number of partitions
N = 1024
# Dimensioned numbers of the set
j = np.zeros((N, N), np.int64)
# constant of the set
#c = np.complex(0.2,0.75)
c = np.complex(0.285, 0.01)
#c = np.complex(-1.037,0.17)
z_real = np.linspace(-2.5, 2.5, N)
z_imag = np.linspace(-2.5, 2.5, N)

# call the function
jit_julia_fractal(z_real, z_imag, j, c)


# plot the fig 
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(j, cmap=plt.cm.inferno, extent=[-1.5, 1.5, -1.5, 1.5])
ax.set_title('Conjunto de Julia para c='+str(c),fontsize=18)
ax.set_xlabel("$\mathrm{Re}(z)$", fontsize=18)
ax.set_ylabel("$\mathrm{Im}(z)$", fontsize=18)
plt.show()

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(j, cmap=plt.cm.jet, extent=[-1.5, 1.5, -1.5, 1.5])
ax.set_title('Conjunto de Julia para c='+str(c),fontsize=18)
ax.set_xlabel("$\mathrm{Re}(z)$", fontsize=18)
ax.set_ylabel("$\mathrm{Im}(z)$", fontsize=18)
plt.show()


fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(j, cmap=plt.cm.hot, extent=[-1.5, 1.5, -1.5, 1.5])
ax.set_title('Conjunto de Julia para c='+str(c),fontsize=18)
ax.set_xlabel("$\mathrm{Re}(z)$", fontsize=18)
ax.set_ylabel("$\mathrm{Im}(z)$", fontsize=18)
plt.show()

