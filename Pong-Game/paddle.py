from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        self.paddle = Turtle("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(x=350, y=0)