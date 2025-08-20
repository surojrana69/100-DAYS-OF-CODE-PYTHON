from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen=Screen()
screen.setup(500,500)
screen.bgcolor("black")
screen.title("Snake Game By Suroj")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()


    #Detect collision with walls0:
    if snake.head.xcor() > 480 or snake.head.xcor() <-480 or snake.head.ycor() > 480 or snake.head.ycor() < -480:
        game_is_on=False
        scoreboard.game_over()

    #Detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()