import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Down", fun=player.down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    chance = random.randint(0, 6)
    if chance == 1:
        car_manager.add_seg()

    car_manager.car_move()

    if player.ycor() > 280:
        player.res_position()
        car_manager.add_speed()
        score.point()

    for segment in car_manager.segments:
        if segment.distance(player) < 20:
            print("ew")
            game_is_on = False



screen.exitonclick()
