#!/usr/bin/env python3
from tkinter import Tk, Canvas

w, h = 1000, 450
win = Canvas(Tk(),width=w,height=h)

def cantor_set(x,y,l):
    if l > 1: # keep doing this while the line is > 1 pixel 
        win.create_line(x,y,x+l,y) # draw horizontal line
        y = y + 50 # move 50 pixels down for next generation
        cantor_set(x,y,l/3) # left hand offspring
        cantor_set(x+2/3*l,y,l/3) # right hand offspring

win.pack()
cantor_set(10,10,w-20)
win.mainloop()




