from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.snakes[0].distance(food) <= 15:
        scoreboard.write_score()
        food.refresh()
        snake.extend()


    # Detect collision with wall.
    if snake.snakes[0].xcor() > 280 or snake.snakes[0].xcor() \
            < -280 or snake.snakes[0].ycor() > 280 or \
            snake.snakes[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    # if head collides with any segments in the tail:
        # trigger game_over
    for segment in snake.snakes[1:]:
        if snake.snakes[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
























screen.exitonclick()