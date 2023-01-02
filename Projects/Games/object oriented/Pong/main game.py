import turtle
import score
import paddle
import ball
import time
import animations

window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Teja's Pong game")
prompt = animations.Anime()

# @
mode = window.textinput(
    title="Game mode", prompt="Enter 1/2 play 1 player or 2 player... = "
)

if mode is "1":
    bot = True
else:
    bot = False

prompt.display_mode(mode)

rpaddle = paddle.Paddle(370, 0)
lpaddle = paddle.Paddle(-370, 0)
for i in range(3):
    prompt.loading()
    prompt.clear()
    time.sleep(0.2)
ball = ball.Ball()
points = score.Score()
# lpoints = score.Score()

window.listen()
window.onkey(rpaddle.goup, "Up")
window.onkey(rpaddle.godown, "Down")
if bot is False:
    window.onkey(lpaddle.goup, "w")
    window.onkey(lpaddle.godown, "s")

game_over = False
while game_over is False:
    ball.move()
    time.sleep(ball.move_speed)

    if bot and ball.xcor() < -300:
        x = lpaddle.xcor()
        y = ball.ycor()
        lpaddle.goto(x, y)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("wall")

    if ball.xcor() > 400:
        ball.replay()
        points.rupdate()

    if ball.xcor() < -400:
        ball.replay()
        points.lupdate()

    if (ball.distance(rpaddle) < 60 and ball.xcor() > 345) or (
        ball.distance(lpaddle) < 60 and ball.xcor() < -345
    ):
        ball.bounce("ball")
        ball.move_speed *= 0.5

window.exitonclick()
