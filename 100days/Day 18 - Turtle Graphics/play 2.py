from random import choice, randint
from turtle import Screen, Turtle
clist=['red','green','cyan','black','orange','yellow'];

tim=Turtle()
for i in range(1,10):
	tim.color(clist[randint(0,len(clist)-1)])
	tim.forward(10)
	tim.penup()
	tim.forward(10)
	tim.pendown()

Screen().exitonclick()