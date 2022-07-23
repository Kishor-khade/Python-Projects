from turtle import Turtle


STARTING_POSITION = (0, -290)
MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
FINISH_LINE = 290


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.goto_start()

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_reached(self):
        if (self.ycor() >= FINISH_LINE):
            return True
        else:
            return False
