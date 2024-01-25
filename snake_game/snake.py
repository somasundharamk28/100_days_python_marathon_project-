from turtle import Turtle,Screen
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in SNAKE_POSITIONS:
            self.add_segments(i)

    def add_segments(self,i):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        tim.goto(i)
        self.segments.append(tim)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)




