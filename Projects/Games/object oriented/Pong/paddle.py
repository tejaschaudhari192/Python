import turtle

class Paddle(turtle.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x,y)
    
    def goup(self):
        x=self.xcor()
        y= self.ycor() +40
        self.goto(x,y)  
    
    def godown(self):
        x=self.xcor()
        y= self.ycor() -40
        self.goto(x,y)