"""Turtle - Tutorial."""

__author__ = "730680410"

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

side_length: int = 300
leo.up()
leo.goto(-145, 120)
leo.down()
leo.color(92, 72, 135)
leo.speed(50)
leo.hideturtle()

i: int = 0
leo.begin_fill()
while (i < 3):
    leo.forward(side_length)
    leo.right(120)
    i += 1
leo.end_fill()


bob: Turtle = Turtle()
bob.hideturtle()
bob.color(0, 0, 0)
bob.up()
bob.goto(-145, 120)
bob.down()
bob.speed(150)


x: int = 0
while x < 3:
    bob.forward(side_length)
    bob.right(120)
    x += 1
done()