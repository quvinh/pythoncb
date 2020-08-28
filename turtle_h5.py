import turtle

x=[100, 270, 80, 0, 120]
y=[-100, 155, 100, 120, 140]
z=["gray","blue","yellow","black","pink"]

f = turtle.Pen()

for i in range(4):
    for j in range(100):
        f.color(z[i])
        turtle.tracer(1,1.5)
        f.speed(0)
        f.left(5)
        f.forward(100)
        f.left(120)
        turtle.update()
    f.up()
    f.setx(x[i])
    f.sety(y[i])
    f.down()
