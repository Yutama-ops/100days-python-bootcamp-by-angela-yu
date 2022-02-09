from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_seg(self):
        random_y = random.randint(-250, 250)
        new_seg = Turtle("square")
        new_seg.turtlesize(stretch_wid=1, stretch_len=2)
        new_seg.color(random.choice(COLORS))
        new_seg.penup()
        new_seg.goto(300, random_y)
        self.segments.append(new_seg)

    def car_move(self):
        for car in self.segments:
            car.backward(self.car_speed)

    def add_speed(self):
        self.car_speed += MOVE_INCREMENT




