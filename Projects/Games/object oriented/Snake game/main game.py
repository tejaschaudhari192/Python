import time
import turtle
import snake
import food
import score

# setting screen
window = turtle.Screen()
window.title("Teja's Snake game")
window.setup(900, 600)
window.tracer(0)  # blank the screen

# lib
player = snake.Snake()
fruit = food.Food()
points = score.Score('white')

# @
theme = window.textinput(
    title="Theme", prompt="Enter theme dark or light...d/l = "
).lower()

if theme == "d":
    window.bgcolor("black")
else:
    window.bgcolor("white")
    points = score.Score("black")

# difficulty level
level = window.textinput(
    title="Difficulty level", prompt="Enter e for easy and h for hard  = "
).lower()
if level == "e":
    speed = 0.25
else:
    speed = 0.1

# controls
window.listen()
window.onkey(player.up, "Up")
window.onkey(player.down, "Down")
window.onkey(player.left, "Left")
window.onkey(player.right, "Right")
game_over = False

# game funtion
while game_over is False:
    window.update()
    player.move()

    # detect collision with food
    if player.mouth.distance(fruit) < 15:
        print("😁")
        fruit.refresh()
        player.extend()
        points.increment()

    time.sleep(speed)

    # self collision
    for seg in player.segments[1:]:
        if player.mouth.distance(seg) < 10:
            game_over = True
            points.gameover()
    # collision with wall
    if (
        player.mouth.xcor() > 450
        or player.mouth.xcor() < -450
        or player.mouth.ycor() > 300
        or player.mouth.ycor() < -300
    ):
        with open("high_score.txt",'w+') as file:
            sc = file.read()
        print(sc)
        game_over = True
        curr_score = points.score
        points.gameover()

window.exitonclick()
