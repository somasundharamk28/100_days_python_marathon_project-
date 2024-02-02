import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S.state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states= data["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_text = screen.textinput(title=f"{len(guessed_states)}/50 states are correct ",prompt = "whats the another states name ").title()
    if answer_text == 'Exit':
        break

    if answer_text in all_states:
        guessed_states.append(answer_text)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_text]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_text)




