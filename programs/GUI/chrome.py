import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Moving Shadow")
screen.bgcolor("white")

# Create the turtle for the shadow
shadow = turtle.Turtle()
shadow.shape("turtle")
shadow.color("gray")
shadow.penup()

# Create the turtle for the main object
main_object = turtle.Turtle()
main_object.shape("turtle")
main_object.color("black")

# Function to move the shadow
def move_shadow():
    shadow.goto(main_object.position())

# Function to move the main object
def move_object():
    main_object.forward(10)
    # Call the function to move the shadow after the main object moves
    move_shadow()

# Keyboard bindings to move the main object
screen.onkey(lambda: main_object.setheading(90), "Up")
screen.onkey(lambda: main_object.setheading(180), "Left")
screen.onkey(lambda: main_object.setheading(0), "Right")
screen.onkey(lambda: main_object.setheading(270), "Down")
screen.listen()

# Main loop
while True:
    move_object()
