from turtle import Turtle, Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.screensize(800, 600)
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))




def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(key="Up", fun=go_up)
screen.onkey(key="Down", fun=go_down)
game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
