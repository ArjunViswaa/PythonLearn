from turtle import Turtle, Screen
from snake2 import Snake
from scoreboard import ScoreBoard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

is_game_on = True
while is_game_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detection of collision turtle head and food
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        is_game_on = False
        scoreboard.write_game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10 :
            is_game_on = False
            scoreboard.write_game_over()

screen.exitonclick()