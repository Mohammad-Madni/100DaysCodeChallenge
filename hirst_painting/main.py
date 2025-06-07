import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
color_list = [(79, 254, 153), (173, 146, 121), (0, 0, 180), (254, 37, 187),
              (149, 56, 251), (157, 106, 56), (218, 254, 102), (254, 147, 201),
              (253, 0, 251), (0, 218, 191), (255, 147, 147), (1, 86, 175), (252, 0, 0),
              (254, 69, 69), (35, 35, 254), (211, 208, 243), (139, 153, 212), (186, 159, 247),
              (238, 106, 204), (0, 212, 217), (251, 138, 0), (136, 0, 254), (147, 230, 235)]

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dotted in range(1, number_of_dots + 1):
    color = random.choice(color_list)
    tim.dot(20,color )
    tim.forward(50)

    if dotted % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()

screen.exitonclick()

