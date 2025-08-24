from time import sleep
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong.exe")
screen.tracer(0)

l_paddle=Paddle((-340,0))
r_paddle=Paddle((340,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"u")
screen.onkey(r_paddle.go_down,"j")




game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Collision with wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    #Collission with  paddle
    if ball.distance(r_paddle) <50 and ball.xcor() > 310 or ball.distance(l_paddle) <50 and ball.xcor() >  -310:
        ball.bounce_x()


    #When right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()



    #when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

