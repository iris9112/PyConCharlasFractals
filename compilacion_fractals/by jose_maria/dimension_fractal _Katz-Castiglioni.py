# -*- coding: utf-8 -*-


"""
Created on Mon May 14 13:51:09 2018

@author:JOSE MARIA MOLINA SANCHEZ
Dimension Fractal
"""

import numpy as np  # importo Numpy
import matplotlib.pyplot as plt #importo MatPlolib



#Dimensión fractal de la curva por el Algoritmo de Katz-Castiglioni
def dimFractal(d):
    medida = np.size(d)
    dist = np.max(d) - np.min(d) # distancia desde el punto (0,0)
    long = np.sum(np.abs(np.ediff1d(d))) # longitud de la curva
    norm = dist / long # distancia maxima normalizada
    return np.log(medida-1) / (np.log(medida-1) + np.log(norm))


t = np.linspace(1,10000-1,10000)
data1 = np.log(np.cumsum(np.random.randn(10000))+10000)
data2 = np.log(np.random.randn(10000)+10000)
data3 = np.log(np.cumsum(np.random.randn(10000)+1)+10000)
data4 = 8 * np.cos(2*np.pi*1.5*t) + 9 * np.cos(2*np.pi*7.5*t)
data5 = 5000*2 - (t - 5000)**2
data6 = 2**(t/10000)

print(dimFractal(data1))
print(dimFractal(data2))
print(dimFractal(data3))
print(dimFractal(data4))
print(dimFractal(data5))
print(dimFractal(data6))

#Gráficas
plt.ion()
plt.figure('Dimensión fractal de la curva por el Algoritmo de Katz-Castiglioni')
plt.clf()
plt.subplots_adjust(bottom=0.06, top=0.97, right=0.97, left=0.05, wspace=0.10, hspace=0.10)

plt.subplot(231)
plt.plot(t, data1, c=(0,0,1), lw=0.5, label='data1. %.2f' %dimFractal(data1))
plt.grid(True, ls='--') # muestro los ejes secundarios
plt.legend()

plt.subplot(232)
plt.plot(t, data2, c=(0,1,0), lw=0.5, label='data2. %.2f' %dimFractal(data1))
plt.grid(True, ls='--') # muestro los ejes secundarios
plt.legend()

plt.subplot(233)
plt.plot(t, data3, c=(1,0,0), lw=0.5, label='data3. %.2f' %dimFractal(data2))
plt.grid(True, ls='--') # muestro los ejes secundarios
plt.legend()

plt.subplot(234)
plt.plot(t, data4, c=(1,1,0), lw=0.5, label='data4. %.2f' %dimFractal(data3))
plt.grid(True, ls='--') # muestro los ejes secundarios
plt.legend()

plt.subplot(235)
plt.plot(t, data5, c=(1,0,1), lw=0.5, label='data5. %.2f' %dimFractal(data4))
plt.grid(True, ls='--') # muestro los ejes secundarios
plt.legend()

plt.subplot(236)
plt.plot(t, data6, c=(0,1,1), lw=0.5, label='data6. %.2f' %dimFractal(data5))
plt.grid(True, ls='--') # muestro los ejes secundarios
plt.legend()


plt.show()
