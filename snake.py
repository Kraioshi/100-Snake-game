from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def level_up(self):
        pog = Turtle()
        pog.shape('square')
        pog.penup()
        pog.color("white")

        last_x = self.segments[-1].xcor()
        last_y = self.segments[-1].ycor()
        prev_x = self.segments[-2].xcor()
        prev_y = self.segments[-1].ycor()
        newest_x = 0
        newest_y = 0

        if last_x == prev_x:
            newest_x = last_x
            if last_y < prev_y:
                newest_y = last_y - 20
            elif last_y > prev_y:
                newest_y = last_y + 20

            pog.goto(newest_x, newest_y)

        if last_y == prev_y:
            newest_y = last_y
            if last_x > prev_x:
                newest_x = last_x + 20
            elif last_x < prev_x:
                newest_x = last_x - 20

            pog.goto(newest_x, newest_y)

        self.segments.append(pog)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # def up(self):
    #     if self.head.xcor() > self.segments[1].xcor():
    #         self.head.left(90)
    #     elif self.head.xcor() < self.segments[1].xcor():
    #         self.head.right(90)
    #     else:
    #         pass
    #
    # def down(self):
    #     if self.head.xcor() < self.segments[1].xcor():
    #         self.head.left(90)
    #     elif self.head.xcor() > self.segments[1].xcor():
    #         self.head.right(90)
    #     else:
    #         pass
    #
    # def left(self):
    #     if self.head.ycor() > self.segments[1].ycor():
    #         self.head.left(90)
    #     elif self.head.ycor() < self.segments[1].ycor():
    #         self.head.right(90)
    #     else:
    #         pass
    #
    # def right(self):
    #     if self.head.ycor() > self.segments[1].ycor():
    #         self.head.right(90)
    #     elif self.head.ycor() < self.segments[1].ycor():
    #         self.head.left(90)
    #     else:
    #         pass
