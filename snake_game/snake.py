from turtle import Turtle


cor = [(0, 0), (-20, 0), (-40, 0)]
mv_dist = 20
UP= 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0] # Create a variable for first segment as head
        
    def create_snake(self):
    # Creates 3 segments for snake
        for i in cor:
            self.add_segment(i)
            
    def add_segment(self,pos):
        self.new_segments = Turtle(shape="square")
        self.new_segments.color("white")
        self.new_segments.penup()
        self.new_segments.setpos(pos)  
        self.segments.append(self.new_segments)
    
    # Function to extend snakes length
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    # Move the snake
    def move(self):
        for i in range(len(self.segments) - 1,0,-1):
            self.new_x = self.segments[i-1].xcor()
            self.new_y = self.segments[i-1].ycor()
            self.segments[i].setpos(self.new_x,self.new_y)
        self.head.forward(mv_dist)
    
    # Control the snake on key press
    # up , down, left and right
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)