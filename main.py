from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.11)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        score.score_add()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            score.reset_score()
            snake.reset_snake()


screen.exitonclick()
