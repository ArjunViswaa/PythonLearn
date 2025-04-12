import random
import turtle as t
from turtle import Turtle, Screen

tim = Turtle()

tim.color("red")
t.colormode(255)

def get_random_color() :
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")

def draw_spirograph(size_of_gap) :
    for _ in range(int(360 / size_of_gap)) :
        tim.color(get_random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(20)
turtle_screen = Screen()
turtle_screen.exitonclick()