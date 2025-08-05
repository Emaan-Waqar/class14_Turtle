import turtle
turtle.Screen().bgcolor("Pink")
square= turtle.Turtle()

sides= 4
length= 100
ang= 360.0/ sides

for i in range(sides):
    square.forward(length)
    square.right(ang)
turtle.done()    