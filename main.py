import time
from turtle import Screen
from bricks import CreateBrick
from paddle import Paddle
from ball import Ball
from score_board import Score
from live_board import Live
# Create Screen
screen = Screen()
screen.title('Breakout')
screen.screensize(canvwidth=400, canvheight=400, bg='black')
screen.tracer(0)

# Create Turtle
create_brick = CreateBrick()
paddle = Paddle()
ball = Ball()
create_brick.__init__()
paddle.__init__()
ball.__init__()
# make brick wall
create_brick.create_bricks()
wall = create_brick.all_bricks
screen.onkey(paddle.go_right, 'Right')
screen.onkey(paddle.go_left, 'Left')
type = screen.textinput('Game mode', "Choose Difficulty level Hard, Easy, Impossible").title()
# write score
score = Score()
# write health status
live = Live()

screen.listen()
game_on = True
while game_on:
    if type == 'Easy':
        time.sleep(1)
    elif type == 'Hard':
        time.sleep(0.1)
    else:
        time.sleep(0)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.xcor() > 360 or ball.xcor() < -340:
        ball.after_wall()
    # detect collision with top
    if ball.ycor() > 270:
        ball.wall_up()
    # detect collision with paddle
    if ball.distance(paddle) < 40:
        ball.after_paddle()
    # detect lose from paddle
    if ball.ycor() < -340:
        ball.__init__()
        paddle.paddle_appear()
        live.live_lost()
    # detect collision with brick
    for brick in wall:
        if ball.distance(brick) < 40:
            brick.goto(-1000, 1000)
            score.brick_break()
    # detect when all lives are lost
    if live.lives <= 0:
        live.game_over()
        game_on = False
    # detect win
    if score.score > 107:
        score.game_won()
        game_on = False
screen.exitonclick()

