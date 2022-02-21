from turtle import Turtle
import random


class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move='True', align="center", font=('Arial', 18, 'normal'))

    def point(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move='True', align="center", font=('Arial', 18, 'normal'))
