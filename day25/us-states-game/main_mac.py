import turtle
import pandas

screen = turtle.Screen()
# pandas = pandas()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
game_is_on = True
city = data['state'].tolist()
x_coor = data['x'].tolist()
y_coor = data['y'].tolist()
Guessed_state = 0
city_g = []
while game_is_on:
    answer_data = screen.textinput(title=f"Guessed State {Guessed_state}/50",
                                   prompt="What's another state's name").title()
    # print(a_data)
    print(city)
    x = ""

    if answer_data == "Exit":
        break

    for City in city:
        # print(City)

        if answer_data == City:
            x_index = city.index(City)
            y_index = city.index(City)
            # print(a_data)

            Guessed_state += 1

            city_guessed = turtle.Turtle()
            city_guessed.color("black")
            city_guessed.penup()
            city_guessed.goto(x_coor[x_index], y_coor[y_index])
            city_guessed.hideturtle()
            city_guessed.write(City, align="center", font=("Courier", 12, "normal"))

            city.remove(City)
            x_coor.remove(x_coor[x_index])
            y_coor.remove(y_coor[y_index])

    if Guessed_state == 50:
        game_is_on = False

    # generate states_to_learn.csv
    new_data = pandas.DataFrame(city)
    new_data.to_csv("states_to_learn.csv")



screen.exitonclick()