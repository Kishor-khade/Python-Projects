""" 
Creating the Snake class to control the snake 
initializing snake , extending snake when it eats food, 
control movements : up, down, right, left, 
"""

from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
LEFT, RIGHT = 180, 0
UP, DOWN = 90, 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].xcor(),
                                  self.segments[i-1].ycor())
        self.head.forward(20)

    def position(self):
        return self.head.position()

    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)