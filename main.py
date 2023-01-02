# import colorgram
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
timmy = Turtle()
#
# rgb_colors = []
# colo = colorgram.extract("img.jpg", 25)
# for c in colo:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     new_colo = (r, g, b)
#     rgb_colors.append(new_colo)
#
# print(rgb_colors)

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
         (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138),
         (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151),
         (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

timmy.penup()
timmy.speed("fastest")
timmy.setheading(220)

timmy.hideturtle()
timmy.forward(300)
timmy.setheading(0)
print(timmy.pos())

for i in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(40)
    timmy.setheading(90)
    timmy.forward(40)
    timmy.setheading(180)
    timmy.forward(400)
    timmy.setheading(0)




screen = Screen()
screen.exitonclick()


