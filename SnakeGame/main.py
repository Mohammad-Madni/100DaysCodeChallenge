from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_postion = [(0, 0), (-20, 0), (-40, 0),]
for position in starting_postion:
    tim = Turtle("square")
    tim.color("white")
    tim.goto(position)


screen.exitonclick()
