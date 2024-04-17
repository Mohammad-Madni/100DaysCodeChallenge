import turtle

screen = turtle.Screen()
screen.title("US State-Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_states = screen.textinput(title="Guess the State", prompt="What's another State's name")
print(answer_states)

screen.exitonclick()
