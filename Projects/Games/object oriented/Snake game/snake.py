import turtle
import time

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.mouth = self.segments[0]

    def create_snake(self):
        for pos in starting_position:
            self.add_seg(pos)

    def add_seg(self, pos):
        teja = turtle.Turtle("square")
        teja.penup()
        teja.color("yellow")
        teja.goto(pos)
        self.segments.append(teja)

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_no - 1].xcor()
            y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(x, y)
        self.mouth.forward(move_distance)

    def up(self):
        self.mouth.setheading(90)

    def down(self):
        self.mouth.setheading(-90)

    def left(self):
        self.mouth.setheading(180)

    def right(self):
        self.mouth.setheading(0)
