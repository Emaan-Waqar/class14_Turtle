import turtle
turtle.Screen().bgcolor("black")

board= turtle.Turtle()
board.color("white")
#First triangle for the star
board.forward(100)  #draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

#Second triangle for the star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()