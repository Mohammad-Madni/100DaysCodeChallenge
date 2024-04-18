import turtle
import pandas
screen = turtle.Screen()
screen.title("US State-Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                     prompt="What's another State's name").title()
    if answer_states in all_states:
        guessed_state.append(answer_states)
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
