"""EX05 - Turtle Scene."""

__author__ = "730680410"

from turtle import Turtle, colormode, done
colormode(255)
runner: Turtle = Turtle()


# This function makes the backdrop for the cabin.
def night_sky(runner: Turtle, x: float, y: float) -> None:
    """Function will be used to make a background scene."""
    runner.hideturtle()
    runner.penup()
    runner.goto(x, y)
    runner.pendown()
    runner.color(21, 7, 92)
    i: int = 0
    side_length = 1000
    runner.begin_fill()
    while i < 2:
        runner.forward(side_length)
        runner.right(90)
        runner.forward(side_length / 2)
        runner.right(90)
        i += 1
    runner.end_fill()


# This function is used for all the trees in the picture.
def tree_base(runner: Turtle, x: float, y: float) -> None:
    """Making tree trunks."""
    runner.hideturtle()
    runner.penup()
    runner.goto(x, y)
    runner.pendown
    runner.color(59, 35, 2)
    width = 50
    height = 150
    i: int = 0
    runner.begin_fill()
    while i < 2:
        runner.forward(width)
        runner.right(90)
        runner.forward(height)
        runner.right(90)
        i += 1
    runner.end_fill()


# This function is used for all the leaves on the trees.
def tree_leaves(runner: Turtle, x: float, y: float) -> None:
    """Making the leaves for the trees."""
    runner.hideturtle()
    runner.penup()
    runner.goto(x, y)
    runner.pendown()
    runner.color(2, 75, 4)
    side_length = 150
    i: int = 0
    runner.begin_fill()
    while i < 3:
        runner.forward(side_length)
        runner.right(-120)
        i += 1
    runner.end_fill()


# The next three functions are used to draw the house.
def house_base(runner: Turtle, x: float, y: float) -> None:
    """Making the base of the house."""
    runner.hideturtle()
    runner.penup()
    runner.goto(125.0, -250.0)
    runner.pendown()
    runner.color(87, 58, 7)
    i: int = 0
    runner.begin_fill()
    while i < 2:
        runner.right(90)
        runner.forward(x * 4)
        runner.right(90)
        runner.forward(y * 5)
        i += 1
    runner.end_fill()


def house_roof(runner: Turtle, x: float, y: float) -> None:
    """Making the roof of the house."""
    runner.hideturtle()
    runner.penup()
    runner.goto(-145.0, y)
    runner.pendown()
    runner.color(47, 32, 4)
    i: int = 0
    runner.begin_fill()
    while i < 3:
        runner.forward(x * 2)
        runner.right(-120)
        i += 1
    runner.end_fill()


def house_door(runner: Turtle, width: float, height: float) -> None:
    """Making a door for the house."""
    runner.hideturtle()
    runner.penup()
    runner.goto(-30.0, -150.0)
    runner.pendown()
    runner.color(41, 27, 1)
    i: int = 0
    runner.begin_fill()
    while i < 2:
        runner.forward(width)
        runner.right(90)
        runner.forward(height)
        runner.right(90)
        i += 1
    runner.end_fill()


# Drawing a cabin in the woods with trees at night.
def main() -> None:
    """Combining all the functions to make a picture."""
    runner: Turtle = Turtle()
    night_sky(runner, -500.0, 250.0)
    house_base(runner, -75.0, 50.0)
    house_door(runner, 50, 100)
    house_roof(runner, 145.0, 15.0)
    tree_base(runner, -250.0, -100.0)
    tree_base(runner, 225.0, -100.0)
    tree_leaves(runner, -300.0, -125.0)
    tree_leaves(runner, 175.0, -125.0)
    done()


__name__ == "__main__"