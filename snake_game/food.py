from turtle import Turtle
import random

# Food class Inherits from Turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 ,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.restart()
    
    def restart(self):
        self.cor_x = random.randint(-270,270)
        self.cor_y = random.randint(-270,270) 
        self.goto(x= self.cor_x , y= self.cor_y)