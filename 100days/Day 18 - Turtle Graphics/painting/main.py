from secrets import choice
from turtle import Turtle, exitonclick
import turtle

clist = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
         (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)
teja = Turtle()
teja.penup()
teja.speed(0)
teja.hideturtle()


def position():
    for i in range(2):
        teja.right(90)
        teja.forward(250)
    teja.setheading(0)


position()

for row in range(10):
    for dot in range(10):
        teja.color(choice(clist))
        teja.forward(50)
        teja.dot(20)
    teja.setheading(180)
    teja.forward(50*10)
    teja.setheading(90)
    teja.forward(50)
    teja.setheading(0)

exitonclick()
