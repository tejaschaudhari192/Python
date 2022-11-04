import random
import turtle

def color ():
	r =  random.randint(0,255)
	g =  random.randint(0,255)
	b =  random.randint(0,255)
	return (r,g,b)
	
dirn = [0,90,180,270]

teja = turtle.Turtle()
teja.shape('turtle')
teja.width(10)
turtle.colormode(255)

for i in range(1,100):
	teja.forward(30)
	teja.setheading(random.choice(dirn))
	teja.color(color())


turtle.exitonclick()