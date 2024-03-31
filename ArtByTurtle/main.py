import turtle
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

for _ in range(15):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
screen = Screen()
screen.exitonclick()

