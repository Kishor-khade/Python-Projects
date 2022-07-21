""" Keeps track of Score 
    Display's score
    Update and refresh score
"""

from turtle import Turtle


class score_board(Turtle):
    score_count = 0

    def __init__(self, position):
        super().__init__()
        self.color("White")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score : {self.score_count}",
                   align="center",
                   font=("Courier", 25, "bold"))

    def update(self):
        self.score_count += 1
        self.refresh()

    def game_over(self, message):
        self.goto(0, 0)
        self.write(f"Game Over \n {message}",
                   align="center",
                   font=("Jamrul", 25, "normal"))
