#####Turtle Intro######

import turtle as t
import random

def move_right(angle):
        tim.forward(5)
        tim.setheading(angle)


tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


tim_motion = [90, 180, 270, 360]
tim.shape("turtle")
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# "SeaGreen"]
tim.color("red")
for x in range(1000):
    move_right(random.choice(tim_motion))
    tim.color(random_color())



screen = t.Screen()
screen.exitonclick()


######## Challenge 1 - Draw a Square ############