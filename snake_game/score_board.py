from turtle import Turtle
ALIGN = "center"
FONT = 'arial'
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.score=0
        self.update()


    def update(self):
        self.write(f"Score : {self.score}", move=False, align=ALIGN, font=(FONT, 20, 'normal'))

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGN, font=(FONT, 20, 'normal'))


    def refresh(self):
        self.clear()
        self.score+=1
        self.update()

