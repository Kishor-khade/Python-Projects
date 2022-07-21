from time import sleep
from turtle import Screen

# User-Defined modules
from paddle import Paddle
from ball import Ball
from score import score_board


# Screen setup
scr = Screen()
scr.title("Pong")
scr.setup(width=1000, height=750)
scr.bgcolor("black")
scr.tracer(0)


# Initializing all modules
l_paddle = Paddle(-450, 0)      # ---> for left one
r_paddle = Paddle(450, 0)       # ---> for right one
ball = Ball()
l_score = score_board((-200, 330))     # ---> for left one
r_score = score_board((200, 330))      # ---> for right one

scr.update()


# Event Listeners
scr.listen()
# for left padddle
scr.onkey(l_paddle.move_up, "w")
scr.onkey(l_paddle.move_down, "s")
# for right paddle
scr.onkey(r_paddle.move_up, "Up")
scr.onkey(r_paddle.move_down, "Down")


is_game_on = True

while is_game_on:

    sleep(ball.move_speed)
    scr.update()
    ball.move()

    # Detect collision with wall and bounce back the ball vertically
    if (abs(ball.ycor()) >= 360):
        ball.vertical_bounce()

    # Detect collision with paddle
    # And make the ball to bounce horizontally and increase the ball speed
    if ((abs(ball.distance(l_paddle)) < 50) or (abs(ball.distance(r_paddle)) < 50)) and (abs(ball.xcor()) > 420):
        ball.horizontal_bounce()
        if (ball.move_speed > 0.01):
            ball.move_speed -= 0.0025

    # Detect when ball goes out of play area from left and right wall
    # recenter the ball to initial position
    # increase the opponent score
    if ball.xcor() < -500:
        ball.reset_position()
        ball.horizontal_bounce()
        r_score.update()

    elif ball.xcor() > 500:
        ball.reset_position()
        ball.horizontal_bounce()
        l_score.update()

    # conclude who wins
    if (r_score.score_count > 4):
        r_score.game_over("Right wins")
        is_game_on = False

    elif (l_score.score_count > 4):
        l_score.game_over("Left wins")
        is_game_on = False


scr.exitonclick()
