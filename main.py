import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
colors = ["light steel blue","cornflower blue","royal blue","green yellow","medium sea green","turquoise", "midnight blue", "dark sea green"]


def draw_shape(side):
    angle = 360 / side
    for _ in range(side):
        tim.forward(80)
        tim.right(angle)


for _ in range(2,11):
    draw_shape(_)
    tim.color(random.choice(colors))


screen = Screen()
screen.exitonclick()