import turtle
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)




screen = Screen()
screen.exitonclick()

