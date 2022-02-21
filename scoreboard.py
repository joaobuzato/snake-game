from turtle import Turtle
import random

ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}",  align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}",  align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
