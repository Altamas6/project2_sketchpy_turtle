import turtle
turtle.bgcolor('black')
a=turtle.Turtle()
colors=["red","dark red"]
for n in range(400):
    a.forward(n+1)
    a.right(89)
    a.pencolor(colors[n%2])
turtle.done()