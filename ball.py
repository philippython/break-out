from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.Starting_x = 50
        self.Starting_y = -220
        self.x_move = 10
        self.y_move = 10
        self.ball = Turtle()
        self.penup()
        self.shape('circle')
        self.color('blue')
        self.goto(self.Starting_x, self.Starting_y)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.speed(1)
        self.goto(new_x, new_y)

    def after_wall(self):
        self.x_move *= -1

    def wall_up(self):
        self.y_move *= -1

    def after_paddle(self):
        self.y_move *= -1
