import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
polygon= turtle.Turtle() #define variable

numSides= 8
sideLength= 70
angle= 360.0/ numSides
#iterate loop for number of sides

for i in range(numSides):
    polygon.forward(sideLength)
    polygon.right(angle)
turtle.done()    