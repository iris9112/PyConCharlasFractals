from numpy import complex, array
from PIL import Image
import colorsys

WIDTH = 1024

def i_to_rgb(i):
  color = 255 * array(colorsys.hsv_to_rgb(i/255.0, 1.0, 0.5))
  return tuple(color.astype(int))
      
def mandelbrot(x, y):
  c0 = complex(x, y)
  c = 0
  for i in range(1, 1000):
    if abs(c) > 2:
      return i_to_rgb(i)
    c = c * c + c0
  return (0, 0, 0)
 
img = Image.new('RGB', (WIDTH, int(WIDTH/2)))
pixels = img.load()
 
for x in range(img.size[0]):
  for y in range(img.size[1]):
    pixels[x,y] = mandelbrot((x - (0.75 * WIDTH))/(WIDTH/4), 
                             (y - (WIDTH/4))/(WIDTH/4))
 
img.show()