# Built-in module
from turtle import Screen
from time import sleep

# User-Defined module
from snake import Snake 
from food import Food
from score import ScoreBoard

# creating the screen and altering it for the game
scr = Screen()
scr.title("The Snake")
scr.bgcolor("black")
scr.setup(width=600, height=600)
scr.tracer(0)           # Turn off showing all activities


# creating the objects from the modules created
snake = Snake()
food = Food()
score = ScoreBoard()
scr.update()             # Update the screen


# Event listeners
scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


is_game_on = True

while is_game_on:

    snake.move()
    scr.update()
    sleep(0.1)
    food_x, food_y = food.position()    # x and y coordinates of food 
    snake_x, snake_y = snake.head.position()    # x and y coordinates of snake head

    # If the food and snake head colloids -> add up score and generate new food 
    if (abs(food_x-snake_x) <= 20) and (abs(food_y-snake_y) <= 20):
        food.refresh()
        score.update()
        snake.extend()

    # To detect the collision of snake and wall -> and finish the game
    if (abs(snake_x) > 290) or (abs(snake_y) > 290):
        is_game_on = False
        score.game_over()
        break

    # To detect the collision of snake head and body -> and finish the game
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            is_game_on = False
            score.game_over()
            break


scr.exitonclick()
