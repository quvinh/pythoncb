import turtle

f = turtle.Pen()
f.shape("turtle")
f.color("blue")
s=40
for i in range(5):
    for j in range(5):
        f.right(144)
        f.forward(s)
        s+=5
