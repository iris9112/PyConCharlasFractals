# matplotlib inline
from numpy import *
from matplotlib import pyplot as plt

def mandelbrot( h,w, maxit=40): #20
        '''
        Returns an image of the Mandelbrot fractal of size (h,w).
        '''
        #y,x = ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
        y,x = ogrid[ -0.25:0.25:h*1j, -1.8:-1.3:w*1j ]
        #y,x = ogrid[ -0.05:0.05:h*1j, -1.5:-1.4:w*1j ]
        c = x+y*1j
        z = c
        divtime = maxit + zeros(z.shape, dtype=int)

        for i in range(maxit):
                z  = z**2 + c
                diverge = z*conj(z) > 2**2            # who is diverging
                div_now = diverge & (divtime==maxit)  # who is diverging now
                divtime[div_now] = i + 100                 # note when
                z[diverge] = 2                        # avoid diverging too much

        return divtime

#plt.figure()
fig = plt.subplots(1,figsize=(20,20))
#s = "The Mandelbrot Set ([-2.0,0.8]x[-0.4,1.4], iterations = 40)"
s = "The Mandelbrot Set ([-1.8,-1.3]x[-0.25,0.25], iterations = 40)"
#s = "The Mandelbrot Set ([-1.5,-1.4]x[-0.05,0.05], iterations = 40)" #"+str(maxit)+")"
plt.title(s)
plt.imshow(mandelbrot(1000,1000)) 
plt.axis('off')
plt.show()