import turtle
import pandas
screen = turtle.Screen()
screen.title("US State-Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_states = screen.textinput(title="Guess the State", prompt="What's another State's name").title()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

if answer_states in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_states]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_states)



# print(states)
# print(int(x_cor_value))
# print(int(y_cor_value))
# print(answer_states)

screen.exitonclick()
