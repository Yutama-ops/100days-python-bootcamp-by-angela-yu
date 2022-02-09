from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

t = Turtle()

t.goto(0, 280)
t.write("Home = ", True, align="center", font=20)



screen.exitonclick()