'''
space key for large jump
u for penup and d for pendown
1 for single step
2 for 2 step
r for right 
. or> for 10 degree right
, or < for 10 degree left

'''

import turtle

turtle.Screen().title('Teja\'s Sketcher')

def backword():
	teja.backward(100)

def forward():
	teja.forward(100)

def right():
	teja.right(90)

def left():
	teja.left(90)

def sr():
	teja.right(10)

def sl():
	teja.left(10)

def one():
	teja.forward(2)

def two():
	teja.forward(5)

def circle():
	teja.circle(50)

def sc():
	teja.circle(5)


teja=turtle.Turtle()
sun=turtle.Screen()
sun.listen()

sun.onkey(forward,'space')
sun.onkey(right,'r')
sun.onkey(left,'l')
sun.onkey(one,'1')
sun.onkey(two,'2')
sun.onkey(sr,'.')
sun.onkey(sl,',')
sun.onkey(circle,'o')
sun.onkey(sc,'0')
sun.onkey(teja.penup,'u')
sun.onkey(teja.pendown,'d')

sun.onkey(backword,'b')
sun.onkey(teja.clear,'c')


turtle.exitonclick()