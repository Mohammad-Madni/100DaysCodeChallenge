import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(500, 400)
user_bet = screen.textinput(title="Make_ur_Bet", prompt="Which Turtle win the race? Enter a color: ")
color = ["purple", "red", "blue", "orange", "yellow", "green"]
y_pos = [-100, -60, -20, 20, 60, 100]
all_turtle = []
for turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtles])
    new_turtle.goto(x=-230, y= y_pos[turtles])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won {winning_color} turtle is the Winner !")
            else:
                print(f"You've lost {winning_color} turtle is the Winner !")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
screen.exitonclick()
