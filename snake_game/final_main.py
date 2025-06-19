from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen =Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black") # Set the background color
screen.title("Snake Game") # Set the title
screen.tracer(0) # Turn off the automatic update for each actions of the turtle , to use screen.update()  

# Game Control switch
game_is_on = True

# Create a snake
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

# Create a loop
while game_is_on:

    screen.update()
    time.sleep(0.1) # Pause the next action for 100 milliseconds
    snake.move() # Move the snake continously
    # Detect the collision of snake with food
    # by using distance function in turtle, we can find the distance between any vecors and a turtle or 
    # distance between two turtles
    # turtle.distance(x,y)  x and y are the coordinates of another urtle or 2D Vector

    if snake.head.distance(food) < 15:
        food.restart()
        snake.extend()
        score.add()
        

    # Detect Collision with the wall
    if snake.head.xcor() >280 or snake.head.ycor() > 280:
        game_is_on = False
        score.game_over()
        
    elif snake.head.xcor() < -280 or snake.head.ycor() <-280:
        game_is_on = False
        score.game_over()
        
    # Detect collision with any segments of snake by its head
    for x in snake.segments[1:]: # slicing
        if snake.head.distance(x) < 10:
            game_is_on= False
            score.game_over()
    
    
        
screen.exitonclick()

# By using turtle.write, you can write on the screen to show your scores
# turtle.write("Object to b wrriteen on screen",move = Tur or false,align = "left/center/right",font = ("fontname",fontsize,"fonttype"))


# Day 21:  Slicing in Python

# list_name[start_index:stop_index:increment]
# [::-1]  - reverse the list

# It works for list and tuples