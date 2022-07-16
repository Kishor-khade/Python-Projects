from turtle import Turtle, Screen

turtle = Turtle()
scr  = Screen()

scr.bgcolor("bisque")


def move_forward():
    """ It moves the turtle forward"""
    turtle.forward(5)

def move_backward():
    """ It moves the turtle backward """
    turtle.backward(5)

def rotate_rightward():
    """ It rotate the turtle right by certain angle"""
    turtle.right(10)

def rotate_leftward():
    """ It rotate the turtle left"""
    turtle.left(10)

def clear():
    """ It clear's the screen"""
    turtle.reset()


scr.listen()
# Event Listeners
scr.onkey(move_forward, "w")
scr.onkey(move_backward, "s")
scr.onkey(rotate_rightward, "d")
scr.onkey(rotate_leftward, "a")
scr.onkey(clear, "c")

scr.exitonclick()