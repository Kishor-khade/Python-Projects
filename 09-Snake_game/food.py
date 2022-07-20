""" 
Creating the food class to control the activities of food 
creating food and moving the food to random place
"""

import random
from turtle import Turtle

"""
class Food:
    food = Turtle("circle")
    def __init__(self):
        self.food.color("red")
        self.food.penup()
        self.food.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.refresh()

    def refresh(self):
        self.food.setposition(random.randint(-280, 280),
                              random.randint(-280, 280))

    def position(self):
        return self.food.position()
    
"""


# Using Inheritance
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.refresh()

    def refresh(self):
        self.setposition(random.randint(-280, 280),
                              random.randint(-280, 280))

