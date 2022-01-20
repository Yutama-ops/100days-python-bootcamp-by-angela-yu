#####Turtle Intro######

import turtle as t

def move_right(angle, x):
    for x in range(x):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
for x in range(4, 9):
    print(x)
    angle = int(360/x)
    move_right(angle, x)
    timmy_the_turtle.pencolor(x/10, x/10, x/10)




screen = t.Screen()
screen.exitonclick()


######## Challenge 1 - Draw a Square ############