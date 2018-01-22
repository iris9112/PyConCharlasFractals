import turtle

def make_fractal(length,langle,rangle,iterations,axiom,target,replace,target2,replace2):
    state = axiom
    turtle.speed(0)

    #make the L-System we want to process
    for i in range(iterations):
        nextState=''
        for character in state:
            if character == target:
                nextState += replace
            elif character == target2:
                nextState += replace2
            else:
                nextState += character
        state = nextState


    turtle.down() #pen down
    turtle.color('red','black') #draw line in red, fill black
    turtle.begin_fill() #set the fill setting

    for move in state: #another way to loop through all the characters in a string
        if move == "F":
            turtle.forward(length)
        elif move == "L":
            turtle.left(langle)
        elif move == "R":
            turtle.right(rangle)

if __name__ == '__main__':
    iterations = 20
    myLen = 5
    
    #JP curve drawing
    make_fractal(myLen,90,90,iterations,'FX','X','XRYFR','Y','LFXLY')

