import turtle as t
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.jpeg', 360)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

rgb = [(248, 237, 243), (234, 246, 239), (235, 240, 247), (196, 153, 117), (139, 71, 89), (145, 81, 69), (61, 97, 127), (225, 215, 109), (136, 165, 184), (187, 145, 159), (34, 20, 15), (20, 26, 41), (133, 176, 148), (191, 93, 81), (45, 24, 33), (54, 123, 94), (186, 88, 104), (15, 25, 19), (83, 156, 112), (223, 172, 184), (227, 175, 167), (103, 44, 60), (50, 56, 94), (168, 207, 185), (167, 158, 66), (60, 155, 174), (111, 122, 155), (97, 49, 44), (178, 188, 214), (152, 207, 219), (221, 219, 20), (25, 94, 68), (78, 71, 42), (18, 88, 101)]
tim = t.Turtle()
tim.penup()
t.colormode(255)
t.setx(-200)
t.sety(-200)


for x in range(0, 9):
    tim.setx(t.xcor())
    tim.sety(x*50 + t.ycor())
    tim.dot(20, random.choice(rgb))
    tim.penup()
    tim.forward(50)
    for _ in range(0, 9):
        tim.dot(20, random.choice(rgb))
        tim.penup()
        tim.forward(50)
    tim.setx(-200)



screen = t.Screen()
screen.exitonclick()