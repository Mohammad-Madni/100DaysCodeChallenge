from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(500, 400)
# user_bet = screen.textinput(title="Make_ur_Bet", prompt="Which Turtle win the race? Enter a color: ")
color = ["purple", "red", "blue", "orange", "yellow", "green"]
y_pos = [-100, -60, -20, 20, 60, 100]
for turtles in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color[turtles])
    tim.goto(x=-230, y= y_pos[turtles])

screen.exitonclick()