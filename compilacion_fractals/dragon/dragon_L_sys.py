import turtle

iterations = 5 #the number of generations
startLength = 200 #Length of the generation 0 line

turtle.up()
turtle.setpos(-startLength*3/2,0)
turtle.speed(0)

#Axiom
Dragon = "F" 

#make the L-System we want to process
for i in range(iterations):
    Dragon = Dragon.replace("F","FLFRFRFFLFLFRF")

turtle.down() 
turtle.color('red')
turtle.begin_fill()

for char in Dragon: 
#another way to loop through all the characters in a string
    if char == "F":
        turtle.forward(startLength / (4 ** (iterations - 1)))
    elif char == "L":
        turtle.left(90)
    elif char == "R":
        turtle.right(90)

turtle.end_fill() 
turtle.mainloop()

