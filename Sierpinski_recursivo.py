import turtle

def sierpinski(side, level):
    turtle.color('green')
    turtle.begin_fill()
    if level == 1:
        for i in range(3):
            turtle.forward(side)
            turtle.left(120)
    else:
        sierpinski(side/2, level-1)
        turtle.forward(side/2)
        sierpinski(side/2, level-1)
        turtle.backward(side/2)
        turtle.left(60)
        turtle.forward(side/2)
        turtle.right(60)
        sierpinski(side/2, level-1)
        turtle.left(60)
        turtle.backward(side/2)
        turtle.right(60)
    turtle.end_fill()

def main():
    myLen = 400
    turtle.up()
    turtle.setpos(-myLen/2,-myLen/2)
    turtle.down()
    sierpinski(myLen, 4)

if __name__ == '__main__':
    main()
    turtle.mainloop()
    
    