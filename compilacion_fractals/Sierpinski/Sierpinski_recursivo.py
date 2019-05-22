import turtle

def sierpinski(side, level):
    turtle.color('green')
    turtle.begin_fill()
    if level == 1:
        # draw a triangle
        for i in range(3):
            turtle.forward(side)
            turtle.left(120)
    else:
        # draw the triangle on the left
        sierpinski(side/2, level-1)
        # move the position to half the length
        turtle.forward(side/2)
        # draw the triangle on the right
        sierpinski(side/2, level-1)
        # returns to the midpoint
        turtle.backward(side/2)
        # change position
        turtle.left(60)
        turtle.forward(side/2)
        turtle.right(60)
        # draw the upper triangle
        sierpinski(side/2, level-1)
        # change position again
        turtle.left(60)
        turtle.backward(side/2)
        turtle.right(60)
    turtle.end_fill()

def main():
    myLen = 400
    turtle.up()
    turtle.setpos(-myLen/2,-myLen/2)
    turtle.down()
    sierpinski(myLen, 5)

if __name__ == '__main__':
    main()
    turtle.mainloop()
    