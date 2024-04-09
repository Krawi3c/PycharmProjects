from turtle import Turtle,Screen


tim = Turtle()

def forward():
    tim.forward(10)
def backwards():
    tim.backward(10)
def counter_clockwise():
    new_heading = tim.heading() +10
    tim.setheading(new_heading)
def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear_the_screen():
    tim.clear()
    tim.penup()
    tim.home()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_the_screen)
screen.exitonclick()