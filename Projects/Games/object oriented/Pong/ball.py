import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')  
        self.color('yellow')
        self.penup()
        self.move_speed=0.2/4
        self.xmove=10
        self.ymove=10
    def move(self):
        x = self.xcor()+ self.xmove
        y = self.ycor()+ self.ymove
        self.goto(x,y)
    
    def bounce(self,object):
        if object is 'ball':
            self.xmove *= -1
        if object is 'wall':
            self.ymove *= -1
    
    def replay(self):
        self.move_speed=0.05
        self.goto(x=0,y=0)
        self.bounce('ball')
        