import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()

tim.color("red")
# Challenge - 4
colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
turtle.colormode(255)

def get_random_color() :
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(200) :
    tim.color(get_random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

turtle_screen = Screen()
turtle_screen.exitonclick()