from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",15,"bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setpos(x=-10,y=270)
        self.pendown()
        self.hideturtle()
        self.displayscore()
    def displayscore(self):
        self.write(f"score: {self.score}",align=ALIGNMENT,font=FONT)
    
    def game_over(self):
        
        self.goto(x=0,y=0)
        self.write(f"Game Over",align=ALIGNMENT,font=("Arial",24,"bold"))
    def add(self):
        self.score += 1
        self.clear()
        self.displayscore()
        