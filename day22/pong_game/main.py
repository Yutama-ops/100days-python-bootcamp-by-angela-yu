from turtle import Screen
from paddle import Paddle
from pong import Ball
from scoreboard import Scoreboard
import time
# create screen
screen = Screen()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
pong = Ball()
score = Scoreboard()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
is_game_on = True

while is_game_on:
    pong.move()
    screen.update()
    time.sleep(pong.move_speed)

    if pong.xcor() > 380:
        pong.reset_pos()
        score.l_point()

    if pong.xcor() < -380:
        pong.reset_pos()
        score.r_point()

    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce()

    if r_paddle.head.distance(pong) < 50 and pong.xcor() > 340 or l_paddle.head.distance(pong) < 50 and pong.xcor() < -340:
        pong.reverse()



    # player paddle

    # computer paddle

    # pong ball

    # make it move

    # score player

    # score computer

    # detect collision with wall and bounce

    # detect collision with paddle and bounce

    # detect with paddle misses

    # keep score


screen.exitonclick()