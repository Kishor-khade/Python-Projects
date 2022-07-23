from turtle import Turtle
import random


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
COLORS = ["red", "blue", "navyblue", "green",
          "yellow", "orange", "brown", "pink",
          "black", "skyblue", "maroon", "grey",
          "lightgreen", "violet", "purple"]


class CarManager:
    
    def __init__(self) -> None:
        self.all_cars = []
        self.moving_distance = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def level_increment(self):
        self.moving_distance += MOVE_INCREMENT

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.moving_distance)
            self.remove_car(car)

    def remove_car(self, car):
        if car.xcor() < -300:
            self.all_cars.remove(car)
            car.clear()
            car.hideturtle()