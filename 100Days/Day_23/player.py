from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_to_starting_point()
        self.setheading(90)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def is_finishline_crossed(self):
        return self.ycor() > 280

    def reset_to_starting_point(self):
        self.goto(STARTING_POSITION)