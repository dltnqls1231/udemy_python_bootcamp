import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0

data = pd.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_states = []


def write_text(answer):
    df = data[data["state"] == answer]
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(int(df.x), int(df.y))
    t.write(answer)
    guessed_states.append(answer)


guessed_yet = []
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        yet_df = pd.DataFrame(guessed_yet)
        yet_df.to_csv("guessed_yet.csv")
        break
    if answer_state in states_list:
        write_text(answer_state)
        score += 1

for state in data["state"].to_list():
    if state not in guessed_states:
        guessed_yet.append(state)