from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make You Bet", prompt="Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tim = []
yh = [-70, -40, -10, 20, 50, 80]
for x in range(len(colors)):
    tim.append(Turtle(shape="turtle"))
    tim[x].penup()
    tim[x].color(colors[x])
    tim[x].goto(x = -230, y = yh[x])

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in tim:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner")
        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)

screen.exitonclick()