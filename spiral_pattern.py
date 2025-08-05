import turtle
myWn= turtle.Screen()
myWn.bgcolor("light blue")   #Background color of the screen
myWn.title("Turtle")
myPen= turtle.Turtle()
size= 0
while True:   #iterate loop
    for i in range(4):
        myPen.fd(size +1)
        myPen.left(90)
        size-= 5
    size+=1    
turtle.done()    