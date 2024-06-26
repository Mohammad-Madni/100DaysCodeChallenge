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
    if answer_states == "Exit":
        #list compreshension added after knowing about it
        missing_states = [state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing_states.csv")
        break
    if answer_states in all_states:
        guessed_state.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_states)




