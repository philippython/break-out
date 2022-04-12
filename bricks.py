from turtle import Turtle
from paddle import Paddle
import random


# create class for brick
STARTING_X = -360
STARTING_Y = 300


class CreateBrick(Turtle):
    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.hideturtle()
        self.xpos = -360
        self.ypos = 280
        self.pro = 54

    def create_bricks(self):
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        random_color = random.choice(colors)

        new_brick = Turtle()
        new_brick.shape('square')
        new_brick.color(random_color)
        new_brick.penup()
        new_brick.speed(0)
        new_brick.shapesize(1, 4)
        new_brick.goto(self.xpos, self.ypos)
        self.all_bricks.append(new_brick)
        if len(self.all_bricks) < self.pro:
            if len(self.all_bricks) % 9 == 0:
                self.ypos -= 30
                self.xpos = -360
                self.create_bricks()
            else:
                self.xpos += 85
                self.create_bricks()

