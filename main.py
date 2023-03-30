from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    snek = Turtle(shape='square')
    snek.penup()
    snek.color('white')
    snek.goto(position)


screen.exitonclick()