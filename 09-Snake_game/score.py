""" 
Creating the Score class to keep track of score value 
displaying score, updating score when the sanke colloids with food
"""

from turtle import Turtle


class ScoreBoard:
    Score = Turtle()
    score_count = 0

    def __init__(self):
        self.Score.penup()
        self.Score.color("white")
        self.Score.goto(x=0, y=270)
        self.Score.hideturtle()
        self.refresh()

    def update(self):
        self.score_count += 1
        self.refresh()

    def refresh(self):
        self.Score.clear()
        self.Score.write(f"Score : {self.score_count}", align="center",
                         font=("Roman New", 20, "normal"))

    def game_over(self):
        self.Score.goto(0, 0)
        self.Score.write("Game Over", align="center",
                         font=("Roman New", 20, "normal"))
