import turtle
from states import States

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = States()

title = ""
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
    if answer_state:
        title = states.create_state(answer_state)
    if answer_state == "Exit":
        game_is_on = False
        states.exit()
screen.exitonclick()
