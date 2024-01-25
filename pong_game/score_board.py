from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score=0
        self.r_score=0
        self.hideturtle()
        self.goto(-100,180)
        self.write(self.l_score,align="center",font=("Courier",80,'normal'))
        self.goto(100, 180)
        self.write(self.r_score,align="center",font=("Courier",80,'normal'))

    def l_miss(self):
        self.clear()
        self.r_score += 1
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, 'normal'))
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, 'normal'))
    def r_miss(self):
        self.clear()
        self.l_score += 1
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, 'normal'))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, 'normal'))


