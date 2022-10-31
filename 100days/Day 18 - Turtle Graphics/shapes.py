from random import randint;		import turtle

colors=['red','green','cyan','black','orange','yellow','blue','brown']
teja=turtle.Turtle()
teja.width(5)

i=3
while i<=10:	
	teja.color(colors[randint(0,len(colors)-1)])
	for sides in range(0,i):
		teja.forward(100)
		teja.right(360/i)
	i+=1

turtle.exitonclick()