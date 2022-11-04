import random, turtle

page = turtle.Screen()
page.setup(500, 400)
clr = ['yellow', 'red', 'green', 'blue', 'orange']

def steps():
    return random.randint(0, 10)

players = []

pos = -100
for i in range(0, 5):
    teja = turtle.Turtle('turtle')
    teja.penup()
    teja.color(clr[i])
    teja.goto(x=-240, y=pos)
    pos += 50
    players.append(teja)

bet = page.textinput(title='Welcome to 1xBET',
                     prompt='Enter color to choose Bet...')

game = False
if bet in clr:
    game = True
else:
    print('wrong input')

while game:
    for i in players:
        i.forward(random.randint(0, 10))

    for j in players:
        if j.xcor() > 240:
            game = False
            if bet == j.pencolor():
                print('You won bachhi')
            else:
                print(f'You lose mad ! Winner is {j.pencolor()}')

page.exitonclick()