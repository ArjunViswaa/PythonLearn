import random
from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("red")
# tim.fd(100)
# tim.right(90)
# tim.fd(100)
# tim.right(90)
# tim.fd(100)
# tim.right(90)
# tim.fd(100)

# Challenge - 2
# for _ in range(15) :
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()


# Challenge - 3
colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(num_sides) :
    angle = 360 / num_sides
    for _ in range(num_sides) :
        tim.forward(100)
        tim.right(angle)

for i in range(3, 11) :
    tim.color(random.choice(colors))
    draw_shape(i)

turtle_screen = Screen()
turtle_screen.exitonclick()