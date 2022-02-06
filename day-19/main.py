from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle Win?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race_turtles = []
is_race_on = False
for i in range(6):
    turtles = Turtle(shape="turtle")
    turtles.color(colors[i])
    turtles.penup()
    turtles.goto(x=-230, y=-100 + i*50)
    race_turtles.append(turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in race_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")
            break




screen.exitonclick()