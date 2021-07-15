from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.hideturtle()

        self.write(f"Score = {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)