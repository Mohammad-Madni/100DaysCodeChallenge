from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(600,600)
screen.tracer(0)
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()



screen.exitonclick()