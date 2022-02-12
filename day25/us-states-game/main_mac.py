import turtle
import pandas

screen = turtle.Screen()
# pandas = pandas()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
game_is_on = True

while game_is_on:
    answer_data = screen.textinput(title="Guess the State", prompt="What's another state's name")
    a_data = answer_data.lower()

    x = ""
    if a_data == x:
        pass

screen.exitonclick()