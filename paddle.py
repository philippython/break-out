from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = Turtle()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(1, 3)
        self.goto(0, -250)

    def go_right(self):
        self.forward(30)

    def go_left(self):
        self.backward(30)

    def paddle_appear(self):
        self.goto(0, -250)
