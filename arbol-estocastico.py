# -*- coding: utf-8 -*-
"""
@author: Mauricio Avilés Cisneros
Instituto Tecnológico de Costa Rica, Escuela de Ingeniería en Computación
maviles@itcr.ac.cr

"""

import turtle
import random

#Variables globales
ANG = 25 #ángulo de inclinación para las ramas
RAND = 30 #factor de aleatoriedad del ángulo de inclinación (grados)
REL = 4/5 #relación entre la rama y las sub ramas
RANDT = 80 #factor de aleatoriedad en el tamaño de las ramas (%)
GROSORTRONCO = 5 #pixeles que se le suman al grosor del árbol
TAMINIC = 100 #tamaño del tronco inicial en pixeles
TAMHOJA = 25 #tamaño de la hoja
ANGHOJA = 65 #ángulo de las puntas de las hojas (180 = círculos)
PROF = 7 #cantidad de niveles en el árbol (más de 10 puede durar mucho dibujándose)
CTRONCO = (51, 51, 0)#(67,120,211) #color del tronco. tres números entre 0 y 255
CTRONCOVAR = 60 #factor de aleatoriedad en el color del tronco
CHOJAS = (0, 204, 102)#(255,90,109) #color de las hojas
CHOJASVAR = 90 #factor de aleatoriedad en el color de las hojas
CFONDO = (255,255,255) #color de fondo

# Función que dibuja un árbol fractal
# Entradas:
# t: tamaño del segmento inicial en pixeles
# d: profundidad total del árbol
# Salidas:
# Dibujo del árbol en pantalla
# Restricciones: no
def arbol(t, d):
    if d==0:
        turtle.forward(t)
        hoja(TAMHOJA, ANGHOJA)
        turtle.penup()
        turtle.back(t)
        turtle.pendown()
        turtle.color(CTRONCO)
        return
    else:
        angulo1 = ANG + random.randrange(-RAND, RAND+1)
        angulo2 = ANG + random.randrange(-RAND, RAND+1)
        tamano = t + t*random.randrange(-RANDT, RANDT+1)/100
        colortronco = variacioncolor(CTRONCO, CTRONCOVAR)
        turtle.color(colortronco)
        turtle.pensize(d+GROSORTRONCO)
        turtle.forward(tamano)
        turtle.left(angulo1)
        arbol(t*REL, d-1)
        turtle.right(angulo1+angulo2)
        arbol(t*REL, d-1)
        turtle.color(colortronco)
        turtle.left(angulo2)
        turtle.penup()
        turtle.back(tamano)
        turtle.pendown()
# Función que dibuja una hoja
# Entradas:
# t: tamaño de la hoja
# a: ángulo de las puntas de las hojas
# Salidas:
# Dibujo de una hoja en la posición actual de la tortuga
# Restricciones: no
def hoja(t, a):
    turtle.color(variacioncolor(CHOJAS, CHOJASVAR))
    turtle.begin_fill()
    turtle.right(a/2)
    turtle.circle(t, a)
    turtle.left(180-a)
    turtle.circle(t, a)
    turtle.left(180-a/2)
    turtle.end_fill()

# Función que genera una variación de un color en RGB
# Entradas:
# color: tupla con tres valores enteros entre 0 y 255
# var: cantidad máxima de variación permitida en los valores RGB
# Salidas:
# Tupla de tres valores enteros entre 0 y 255 que es una variación
# del color original.
# Restricciones: no
def variacioncolor(color, var):
    Rd = random.randrange(-var, var+1)
    Gd = random.randrange(-var, var+1)
    Bd = random.randrange(-var, var+1)
    R, G, B = color
    R += Rd
    G += Gd
    B += Bd
    if R > 255:
        R = 255
    elif R < 0:
        R = 0
    if G > 255:
        G = 255
    elif G < 0:
        G = 0
    if B > 255:
        B = 255
    elif B < 0:
        B = 0
    return R, G, B

# Función que inicializa la posición de la tortuga e invoca a la función
# de dibujar árbol fractal.
def init():
    turtle.speed(0)
    turtle.colormode(255)
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.back(200)
    turtle.pendown()
    turtle.hideturtle()
    turtle.color(CTRONCO)
    turtle.bgcolor(CFONDO)
    arbol(TAMINIC, PROF)
    turtle.done()
    turtle.mainloop()

init()