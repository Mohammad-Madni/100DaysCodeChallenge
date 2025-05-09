import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_left():
    tim.left(10)


#move_right_func
def move_right():
    tim.right(10)

#move_forward
def move_forward():
    tim.forward(10)

#move_backward
def move_backward():
    tim.backward(10)

#reset_func
def reset():
    tim.reset()

# Implementation_of_function

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=reset)


screen.exitonclick()
