from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
segments = []

starting_postion = [(0, 0), (-20, 0), (-40, 0),]

for position in starting_postion:
    tim = Turtle("square")
    tim.penup()
    tim.color("white")
    tim.goto(position)
    segments.append(tim)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments) -1, 0, -1):
        x_cor = segments[seg - 1].xcor()
        y_cor = segments[seg - 1].ycor()
        segments[seg].goto(x=x_cor, y=y_cor)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
