from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.up()
leo.goto(-145, 120)
leo.down()
leo.color(92, 72, 135)

i: int = 0
leo.begin_fill()
while (i < 3):
    leo.forward(300)
    leo.right(120)
    i += 1
leo.end_fill()
done()