import random
import turtle
from turtle import Turtle, Screen
import colorgram
# my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("blue")
# turtle.colormode(255)

def color_changing():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    coloring = (r, g, b)
    return coloring

# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

# for _ in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

# color = ["black", "grey", "blue", "orange", "yellow", "pink", "red"]
# def check(no_of_steps):
#     steps = int(360 / no_of_steps)
#     for _ in range(no_of_steps):
#         my_turtle.forward(100)
#         my_turtle.right(steps)
# for taking_steps in range(3, 11):
#     my_turtle.color(random.choice(color))
#     check(no_of_steps = taking_steps)
# my_turtle.speed("fastest")
# my_turtle.pensize(10)
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     my_turtle.color(color_changing())
#     my_turtle.forward(30)
#     my_turtle.setheading(random.choice(directions))


# def draw_spirograph(degree):
#     for _ in range(int(360/ degree)):
#         my_turtle.color(color_changing())
#         my_turtle.circle(100)
#         my_turtle.setheading(my_turtle.heading() + degree)
#
#
# draw_spirograph(5)
# rgb_colors = []
# colors = colorgram.extract('hirst_dot_painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
color_list = [(79, 254, 153), (173, 146, 121), (0, 0, 180), (254, 37, 187), (149, 56, 251), (157, 106, 56), (218, 254, 102), (254, 147, 201), (253, 0, 251), (0, 218, 191), (255, 147, 147), (1, 86, 175), (252, 0, 0), (254, 69, 69), (35, 35, 254), (252, 229, 246), (211, 208, 243), (139, 153, 212), (186, 159, 247), (238, 106, 204), (0, 212, 217), (251, 138, 0), (136, 0, 254), (147, 230, 235)]


print(rgb_colors)



#
# screen = Screen()
# screen.exitonclick()

