import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-430, 430)
        self.goto(x, y)
