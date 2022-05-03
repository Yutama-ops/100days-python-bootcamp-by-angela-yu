import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
guessed = 0
# get coordinates on mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

answer_state = screen.textinput(title="Guess the State", prompt="Whats another state's name?")
data = pandas.read_csv("50_states.csv")
while game_is_on:

    answer_data = screen.textinput(title=f"State Guessed {guessed}/50", prompt="What's another state's name")
    a_data = answer_data.lower()

    x = data[data["state"] == a_data]
    if a_data == x:
        guessed += 1


screen.exitonclick()
