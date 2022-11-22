import time
from turtle import Screen, Turtle

window = Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('Teja\'s Snake')

window.tracer(0)

posn = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for p in posn:
    seg = Turtle('square')
    seg.color('yellow')
    seg.goto(p)
    snake.append(seg)


run = True


while run:
    window.update()
    for p in snake:
        p.forward(5)
        time.sleep(0.01)
    for num in range(2,0,-1):
        p.left(90)

    
    

window.exitonclick()
# ̥̥
