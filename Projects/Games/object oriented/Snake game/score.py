from turtle import Turtle

class Score(Turtle):
    def __init__(self,tc):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color(tc)
        self.goto(250,340)
        self.clear
        self.write(arg=f"Score : {self.score}", font=("Arial", 15, "normal"))

    def increment(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score : {self.score}", font=("Arial", 15, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write("Game over", font=("Arial", 20, "normal"))
