import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
tim.pensize(15)
tim.speed("fastest")
direction = [0, 90, 180, 270]

for i in range(500):
    random_direction = random.choice(direction)
    color_r = random.randint(0, 256)
    color_g = random.randint(0, 256)
    color_b = random.randint(0, 256)
    tim.forward(30)
    tim.setheading(random_direction)
    tim.pencolor(color_r, color_g, color_b)

screen = Screen()
screen.exitonclick()

