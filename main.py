
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
from watermark import Watermark

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
watermark = Watermark()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend_snake()
        food.refresh()
        score.increase_score()
    # detect collison with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        score.reset()


    #detection with its own tail
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            snake.reset()
            score.reset()


screen.exitonclick()
