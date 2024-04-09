from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")

class Score(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=("Verdana", 30, "normal"))
