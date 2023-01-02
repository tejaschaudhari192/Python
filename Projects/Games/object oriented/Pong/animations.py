import turtle
import time

class Anime(turtle.Turtle):
    def __init__(self) :
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        
    def loading(self):
        for i in range(3):
            self.goto(-100,250)
            self.write(arg='Loadming...', font=('courier', 30, 'bold'))
    
    def display_mode(self,mode):
        self.goto(-200,0)
        self.write(arg=f'You have chosen {mode} Player mode', font=('courier', 20, 'bold'))
    
    

