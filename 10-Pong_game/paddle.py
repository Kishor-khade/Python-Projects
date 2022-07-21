""" Here all the functinalities associated with paddle are declared
    Move paddle up and down 
"""


from turtle import Turtle


class Paddle(Turtle):   # used inheritance

    def __init__(self, x, y):
        super().__init__()
        self.x_position = x
        self.y_position = y
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(self.x_position, self.y_position)
        pass

    def move_up(self):
        if (self.y_position <= 280):
            self.y_position += 20
            self.goto(self.x_position, self.y_position)

    def move_down(self):
        if (self.y_position >= -280):
            self.y_position -= 20
            self.goto(self.x_position, self.y_position)
