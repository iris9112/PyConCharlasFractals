#!/usr/bin/env python3
import turtle
from random import randint

def draw_square(length, iterations):
    turtle.bgcolor('black')
    turtle.speed(0)
    x = 1
    while x < iterations:
	# makes variables r,g,b whose value is an integer
        r = randint(0,255) 
        g = randint(0,255) 
        b = randint(0,255) 
        
        turtle.colormode(255)
     # changes every time the loop runs		
        turtle.pencolor(r,g,b)  
		
        turtle.forward(length)
        turtle.right(92)
        draw_square(length+x, iterations-1)
        
draw_square(100, 100)
turtle.mainloop()

