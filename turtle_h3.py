import turtle

f = turtle.Pen()
f.color("yellow")
f.speed(0)
x=50
for i in range(50):
    f.circle(x)
    x-=1

ff = turtle.Pen()
ff.color("red")
ff.circle(51)
