from time import sleep
from turtle import Screen

from player import Player
from score import ScoreBoard
from cars import CarManager


#screen setup
scr = Screen()
scr.setup(width=600, height=620)
scr.title("Turtle Crossing game")
scr.tracer(0)


# Initializing objects
player = Player()
score = ScoreBoard()
car_manager = CarManager()


#Event listeners
scr.listen()
scr.onkey(player.move, "Up")


is_game_on = True
while is_game_on:

    car_manager.create_car()
    car_manager.move_cars()

    # If car is reached finish line then level up
    if player.is_reached():
        player.goto_start()
        car_manager.level_increment()
        score.update()

    # Detect the collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            break

    scr.update()
    sleep(0.1)


score.game_over()
scr.exitonclick()
