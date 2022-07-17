from turtle import Turtle, Screen
import random

scr = Screen()
scr.setup(600, 500)
user_color = scr.textinput(
    title="Welcome to Turtle",
    prompt="Which turtle will win the race .\nchoices : [red, blue, green, yellow, orange, black, brown, purple] \nchoose the color : "
)


is_game_over = False
all_turtle = []
colors = ['red', 'blue', 'green', 'yellow',
          'orange', 'black', 'brown', 'purple']

for i in range(8):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(random.choice(colors))
    colors.remove(new_turtle.pencolor())
    new_turtle.penup()
    new_turtle.goto(x=-280, y=200-50*(7.5-i))
    all_turtle.append(new_turtle)


while not is_game_over:
    for turtle in all_turtle:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 240:
            winning_color = turtle.pencolor()
            is_game_over = True
            break

if user_color.lower() == winning_color:
    print(f"You've Won!. The {winning_color} turtle is the winner")
else:
    print(f"You've lost. The {winning_color} turtle is the winner")

scr.exitonclick()
