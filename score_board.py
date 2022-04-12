from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-380, 300)
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score}', align='left', font=('Arial', 10, 'normal'))

    def brick_break(self):
        self.score += 2
        self.update()
        self.write(f'Score: {self.score}', align='left', font=('Arial', 10, 'normal'))

    def game_won(self):
        game = Turtle()
        game.penup()
        game.color('white')
        game.hideturtle()
        game.goto(0, 0)
        game.write(arg="CONGRATULATIONS YOU HAVE BROKEN ALL BRICKS", align="center", font=('Arial', 10, 'normal'))
