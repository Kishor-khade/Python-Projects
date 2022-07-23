from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        self.level = 1
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-230, 250)
        self.refresh()
        self.hideturtle()

    def refresh(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center",
                   font=("Courier", 18, "normal"))

    def update(self):
        self.level += 1
        self.refresh()
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 25, "bold"))
