from tkinter import *
import math

# Draws a fractal Sierpinski triangle.
# Parameters:
#   canvas: a canvas on which to draw on
#   x, y: coordinates of the lower left corner of the triangle
#   size: lenght of the side of the triangle
#   level: depth of recursion, integer >= 0
def sierpinski(canvas, x, y, size, level):
    x = float(x)
    y = float(y)
    # base case: a Sierpinsky triangle at level 0
    # is just a solid triangle
    if (level == 0):
        canvas.create_polygon(x, y, x+size, y,
                              x+size/2, y-size*math.sqrt(3)/2,
                              fill="black")
    # recursive case: shrink the previous level of Sierpinski
    # triangle, and repeat it three times
    else:
        sierpinski(canvas, x, y, size/2, level-1)
        sierpinski(canvas, x+size/2, y, size/2, level-1)
        sierpinski(canvas, x+size/4, y-size*math.sqrt(3)/4,
                   size/2, level-1)

root = Tk()
myCanvas = Canvas(root, width=600, height=600)
myCanvas.pack()
sierpinski(myCanvas, 50, 500, 500, 6)
root.mainloop()