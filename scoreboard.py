from turtle import Turtle, Screen
from os import path

FONT = ('Courier', 14, 'bold')
GAME_OVER = ('Courier', 24, 'bold')
ALIGNMENT = 'center'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.speed("fastest")
        self.penup()
        self.goto(0, 274)
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", font=FONT, align=ALIGNMENT)

    def score_add(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()


if __name__ == '__main__':
    board = ScoreBoard()
    board.score_add()

    screen = Screen()
    screen.exitonclick()
