#!/usr/bin/env python3
from turtle import *

# Draw a Koch snowflake
def koch(a, order):
    if order > 0:
        # A line Koch for the first generation
        for i in [60, -120, 60, 0]:
            koch(a/3, order-1)
            left(i)
    else:
        forward(a)

def koch_curve(size, order):    
    # Choose colours and size    
    color('black', 'skyblue')
    # Ensure snowflake is centered
    penup()
    backward(size/1.5)
    left(60)
    pendown()
    begin_fill() #set the fill setting
    # Koch curve
    for i in range(3):
        koch(size, order)
        right(120)
    end_fill() #fill any enclosed areas
    
koch_curve(300, 3)    

# Make the last parts appear
update()
mainloop()

