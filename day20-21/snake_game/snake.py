from turtle import Turtle
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        self.segments.append(Turtle(shape="square"))
        self.segments[-1].color("white")
        self.segments[-1].penup()
        self.segments[-1].goto(position)

    def add_snake(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for t in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[t - 1].xcor()
            new_y = self.segments[t - 1].ycor()
            self.segments[t].goto(new_x, new_y)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)