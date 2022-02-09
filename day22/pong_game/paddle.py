from turtle import Turtle
UP = 90
DOWN = 270
WIDTH = 1.0
HEIGHT = 5.0
FORWARD = 20


class Paddle:
    def __init__(self, position):
        self.segment = []
        self.create_paddle()
        self.head = self.segment[0]
        self.head.goto(position)

    def create_paddle(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.segment.append(new_segment)

    def up(self):
        if self.head.ycor() < 260:
            cur_y = self.head.ycor()
            self.head.sety(cur_y + 20)

    def down(self):
        if self.head.ycor() > -260:
            cur_y = self.head.ycor()
            self.head.sety(cur_y - 20)
