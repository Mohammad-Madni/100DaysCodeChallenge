import random
import turtle
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

# for _ in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

color = ["black", "grey", "blue", "orange", "yellow", "pink", "red"]
def check(no_of_steps):
    steps = int(360 / no_of_steps)
    for _ in range(no_of_steps):
        my_turtle.forward(100)
        my_turtle.right(steps)
for taking_steps in range(3, 11):
    my_turtle.color(random.choice(color))
    check(no_of_steps = taking_steps)

screen = Screen()
screen.exitonclick()

