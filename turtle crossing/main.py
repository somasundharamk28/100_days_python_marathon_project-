import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scores = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car = CarManager()
screen.listen()
screen.onkey(tim.move_forward,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car.multiple_car()
    car.move_car()
    for i in car.all_car:
        if i.distance(tim) < 20:
            scores.game_over()
            game_is_on = False
    if tim.ycor() > 300:
        scores.score_up()
        tim.restart_position()
        car.level_up()


screen.exitonclick()
