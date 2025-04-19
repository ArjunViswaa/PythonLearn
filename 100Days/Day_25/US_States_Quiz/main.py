import turtle
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()
    print(answer_state)
    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        print(missed_states)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
# screen.exitonclick()