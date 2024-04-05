from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0),]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            tim = Turtle("square")
            tim.penup()
            tim.color("white")
            tim.goto(position)
            self.segments.append(tim)
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=x_cor, y=y_cor)
        self.segments[0].forward(MOVE_DISTANCE)