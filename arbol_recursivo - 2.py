# -*- coding: utf-8 -*-
import turtle
import math

scene = turtle.Screen()
scene.tracer(200)

tree = turtle.Turtle()
tree.color("green")
tree.speed(0)

def drawSquare(t, size):
  t.begin_fill()
  for i in range(4):
    t.forward(size)
    t.left(90)
  t.end_fill()

def drawNode(t, size, angle, level):
  if (level < 1):
    return
  else:
    drawSquare(t, size)
    
    angleRad = angle * math.pi / 180
    
    # Left Branch
    leftSize = size * math.sin(angleRad)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.right(90 + angle)
    t.forward(leftSize)
    t.left(90)
    drawNode(t, leftSize, angle, level - 1)
    
    # Right Branch
    rightSize = size * math.cos(angleRad)
    t.right(180)
    t.forward(rightSize)
    t.left(90)
    drawNode(t, rightSize, angle, level - 1)
    t.left(angle)
    t.back(size)
  
# Position the turtle, and start drawing!
tree.penup()
tree.goto(30, -150)
tree.left(90)
tree.pendown()
  
drawNode(tree, 100, 45, 12)   # Turtle, inital side length, angle, depth

tree.hideturtle()
tree.mainloop()