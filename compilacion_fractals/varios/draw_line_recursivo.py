#!/usr/bin/env python3
from tkinter import *

master = Tk()

w = Canvas(master, width=1050, height=200)
w.pack()

def drawLines(x1, y1, x2, y2):
    w.create_line(x1,y1,x2,y2)
    
    dx = x2-x1
    dy = y2-y1
    
    if dx == 0 and dy > 4:
        drawLines(x1-dy/3,y1,x1+dy/3,y1)
        drawLines(x1-dy/3,y2,x1+dy/3,y2)
    elif dy == 0 and dx > 4:
        drawLines(x1,y1-dx/3,x1,y1+dx/3)
        drawLines(x2,y1-dx/3,x2,y1+dx/3)
          
    
drawLines(100,100,700,100)
master.mainloop()



