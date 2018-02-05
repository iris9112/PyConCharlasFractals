#!/usr/bin/env python3
from tkinter import Tk, Canvas

w, h = 1000, 450
win = Canvas(Tk(),width=w,height=h)

def cantor(x,y,l):
	# keep doing this while the line is > 1 pixel
    if l > 1:
        # draw horizontal line  
        win.create_line(x,y,x+l,y) 
        # move 20 pixels down for next generation
        y = y + 20 
        # left hand offspring
        cantor(x,y,l/3) 
        # right hand offspring
        cantor(x+2/3*l,y,l/3) 

win.pack()
cantor(10,10,w-20)
win.mainloop()
