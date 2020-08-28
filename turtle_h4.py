import turtle

f = turtle.Pen()

f.speed(0)

for i in range(50):
    if i%2==0:
        f.color("blue")
    else:
        f.color("red")

    f.circle(i)
    f.left(1/2*i)

