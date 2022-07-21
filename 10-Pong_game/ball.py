""" Initializing ball, automating ball movements,
    make ball bounce in horizontal and vertical direction
"""

from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        pass

    def move(self):
        self.goto(self.xcor() + self.x_move,
                  self.ycor() + self.y_move)

    def vertical_bounce(self):
        self.y_move *= -1

    def horizontal_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
