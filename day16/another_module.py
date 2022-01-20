# from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
#
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)
# timmy.tilt(90)
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon name", ["pikachu", "charmeleon", "bulbasour"], "l")
table.add_column("Pokemon type", ["thunder", "fire", "earth"], "l")

print(table)
