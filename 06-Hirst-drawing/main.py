import random
from turtle import Screen, Turtle

# To detect the colors from the picture --> hirst
# import colorgram
# colors = colorgram.extract("hirst-1.jpeg", 40)

# i = 0
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors[i] = (r, g, b)
#     i += 1
# print(colors)


colors = [
    (230, 228, 224), (236, 241, 238), (241,
                                       236, 240), (198, 159, 116), (70, 92, 129),
    (147, 85, 53), (218, 210, 116), (138, 160,
                                     191), (178, 160, 38), (184, 146, 164),
    (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79),
    (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94),
    (177, 96, 114), (102, 119, 170), (34, 52,
                                      45), (100, 160, 85), (214, 175, 192),
    (216, 181, 173), (160, 209, 191), (67,
                                       86, 23), (219, 206, 8), (181, 186, 213),
    (46, 72, 57), (168, 201, 212), (100, 137, 144)
]


turtle = Turtle()
scr = Screen()

scr.colormode(255)
turtle.setheading(225)
turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")
turtle.forward(350)
turtle.setheading(0)

for i in range(1,101):
    turtle.forward(50)
    turtle.dot(20, random.choice(colors))

    if i % 10 == 0:
        turtle.backward(10*50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)

scr.exitonclick()
