import colorgram
import turtle as t
import random

t.colormode(255)
colors = colorgram.extract('image.jpg', 30)
my_colors = []
for color in colors:
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    my_colors.append((r, g, b))
pen = t.Turtle()
pen.penup()
pen.setposition(-200, -200)
pen.hideturtle()

for i in range(1, 11):
    for _ in range(10):
        pen.color(random.choice(my_colors))
        pen.pendown()
        pen.dot(20)
        pen.penup()
        pen.forward(50)
    pen.setposition(-200, -200 + 50 * i)

screen = t.Screen()
screen.exitonclick()