import turtle

class Score(turtle.Turtle):
    def __init__(self) :
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.rscore = 0
        self.lscore = 0
        self.board()

    def board(self):
        self.clear()
        self.goto(100,250)
        self.write(self.lscore,font=('courier',20,'normal'))
        self.goto(-100,250)
        self.write(self.rscore,font=('courier',20,'normal'))
    
    def lupdate(self):
        self.lscore+=1
        self.board()
    def rupdate(self):
        self.rscore+=1
        self.board()
        