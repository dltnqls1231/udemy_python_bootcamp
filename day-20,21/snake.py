from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        body = Turtle(shape="square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.snakes.append(body)

    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.snakes[-1].position())

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(270)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(0)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(180)