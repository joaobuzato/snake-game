from turtle import Turtle
import random

ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score} / High Score: {self.high_score}",  align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} / High Score: {self.high_score}",  align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", 'w') as data:
                data.write(f"{self.score}")
            self.high_score = self.score

        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
