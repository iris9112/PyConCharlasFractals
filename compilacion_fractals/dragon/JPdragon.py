import turtle

def make_fractal(length,langle,rangle,iterations,axiom,target,replace,target2,replace2):
    state = axiom
    turtle.speed(0)

    #make the --System we want to process
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
	#draw line in red
    turtle.color('red') 
 

    for move in state: 
        if move == "F":
            turtle.forward(length)
        elif move == "-":
            turtle.left(langle)
        elif move == "+":
            turtle.right(rangle)
    
if __name__ == '__main__':
    iterations = 9
    mylen = 10
    
    #JP curve drawing
    make_fractal(mylen,90,90,iterations,'FX','X','X+YF+','Y','-FX-Y')
    turtle.mainloop()

	
