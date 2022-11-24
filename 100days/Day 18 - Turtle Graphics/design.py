import random
import turtle


def color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# angle = int(input("Enter size of shift : "))
angle = 5# Distance between circles

turtle.colormode(255)
teja = turtle.Turtle()
teja.speed('fastest')

n = no_of_circles = 360//angle

for i in range(1, n):
    teja.circle(100)
    teja.left(angle)
    teja.color(color())

turtle.exitonclick()
