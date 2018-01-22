# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:35:55 2018

dibujando arboles mas realistas

La idea básica de este fractal es muy simple, se empieza con una línea que es el tronco del árbol y que se divide en dos ramas más pequeñas. 
Ese mismo proceso se repite para cada una de las ramas hasta llegar a una cantidad límite de divisiones (profundidad del árbol). 
Como las ramas del árbol siempre se dividen en dos sub-ramas, el resultado es un árbol binario.

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






