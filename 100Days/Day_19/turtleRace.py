import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win in the race ?")
colors = ["red", "violet", "blue", "green", "yellow", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6) :
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet :
    is_race_on = True

while is_race_on :
    for turtle in all_turtles :
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower() :
                print(f"You've won! The {winning_color} turtle is the winner !!")
            else :
                print(f"You've lost! The {winning_color} turtle is the winner...")

screen.exitonclick()