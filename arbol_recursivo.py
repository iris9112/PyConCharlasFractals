# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:35:55 2018
@author: iris9112
"""
import turtle

turtle.left(90)

def arbol(tam, prof):
    if prof==0:
        return
    else:
        turtle.forward(tam)
        turtle.left(45)
        arbol(tam*2/3, prof-1)
        turtle.right(90)
        arbol(tam*2/3, prof-1)
        turtle.left(45)
        turtle.back(tam)

arbol(120, 10)        
turtle.mainloop()





