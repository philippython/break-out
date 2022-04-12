from turtle import Turtle


class Live(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 5
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(300, 300)
        self.update_live()

    def update_live(self):
        self.clear()
        self.write(f'Lives: {self.lives}', align='left', font=('Arial', 10, 'normal'))

    def live_lost(self):
        self.lives -= 1
        self.update_live()
        self.write(f'Lives: {self.lives}', align='left', font=('Arial', 10, 'normal'))

    def game_over(self):
        game = Turtle()
        game.penup()
        game.color('white')
        game.hideturtle()
        game.goto(0, 0)
        game.write(arg="GAME OVER.", align="center", font=('Arial', 10, 'normal'))
