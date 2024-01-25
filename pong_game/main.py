from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time
screen = Screen()
scoreboard = ScoreBoard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
c_ball = Ball()




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    c_ball.move()
    time.sleep(c_ball.move_speed)
    screen.update()
    if c_ball.ycor()>280 or c_ball.ycor()<-280:
        c_ball.bounce_y()

    if c_ball.distance(r_paddle) < 50 and c_ball.xcor()>320 or c_ball.distance(l_paddle) < 50 and c_ball.xcor()<-320:
        c_ball.bounce_x()

    if c_ball.xcor()> 380:
        scoreboard.r_miss()
        c_ball.reset_ball()


    if c_ball.xcor()<-380:
        scoreboard.l_miss()
        c_ball.reset_ball()







screen.exitonclick()