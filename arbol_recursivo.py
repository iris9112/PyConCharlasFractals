# -*- coding: utf-8 -*-
import turtle

def tree(size, level):
    turtle.color('green')
    turtle.pensize(2)
    turtle.speed(0)
	
    if level == 0:
        return
    else:
        turtle.forward(size)
        turtle.left(45)
        tree(size*2/3, level-1)
        turtle.right(90)
        tree(size*2/3, level-1)
        turtle.left(45)
        turtle.backward(size)

turtle.left(90)
tree(100, 7)        
turtle.mainloop()






		
		
	
	