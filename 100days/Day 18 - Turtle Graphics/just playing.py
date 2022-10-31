import turtle

#defining shape
object = turtle.Turtle()
object.shape('turtle')
object.color('blue')

#motion
# object.forward(100)
# object.right(90)
# object.forward(100)
# object.right(90)
# object.forward(100)
# object.right(90)
# object.forward(100)
#effective approach

for i in range(1,5):
	object.right(90)
	object.forward(100)

turtle.exitonclick()