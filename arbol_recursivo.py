# -*- coding: utf-8 -*-
import turtle

turtle.left(90)
turtle.color('green')
turtle.pensize(5)

def arbol(tam, prof):
    turtle.speed(0)
    if prof == 0:
        return
    else:
        turtle.forward(tam)
        turtle.left(45)
        arbol(tam*2/3, prof-1)
        turtle.right(90)
        arbol(tam*2/3, prof-1)
        turtle.left(45)
        turtle.back(tam)

arbol(100, 12)        
turtle.mainloop()





