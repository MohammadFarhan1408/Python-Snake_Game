from turtle import Turtle

FONT = ('DejaVu Sans Bold', 16, 'normal')
ALIGN = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            data = file.read()
            self.high_score = int(data)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)
        self.goto(180, 270)
        self.write(f'High Score: {self.high_score}', align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', align=ALIGN, font=FONT)
