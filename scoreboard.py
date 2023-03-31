from turtle import Turtle, Screen

FONT = ('Courier', 14, 'bold')
GAME_OVER = ('Courier', 20, 'bold')
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
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def score_add(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=GAME_OVER, align=ALIGNMENT)


if __name__ == '__main__':
    board = ScoreBoard()
    board.score_add()

    screen = Screen()
    screen.exitonclick()
