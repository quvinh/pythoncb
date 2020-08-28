import turtle
from itertools import cycle
pen=turtle.Turtle()
pen.color('blue')
pen.speed(15)
COLOR_NAMES = ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow','black']

colors = cycle(COLOR_NAMES)

for i in range (181):
    if(i==60):
        pen.color('red')
    if(i==120):
        pen.color('yellow')
    if(i==180):
        pen.color('magenta')
    pen.forward(100)
    pen.right(30)
    pen.forward(20)
    pen.left(60)
    pen.forward(50)
    pen.right(30)
   
    
    pen.penup()
    pen.setposition(0,0)
    pen.pendown()
    
    pen.right(2)

turtle.done()
