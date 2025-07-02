from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(x = -270, y = 250)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.score}", font=FONT)
        self.score += 1
