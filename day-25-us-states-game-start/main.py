import turtle
from input_manager import InputManager

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

input_manager = InputManager()

game_is_on = True
guesses = 0
while game_is_on:
    answer_state = screen.textinput(title=f"{guesses}/50 States Correct", prompt="What's another states name's?").title()
    if input_manager.answer_check(answer_state):
        guesses += 1

    if answer_state == "Game Over":
        game_is_on = False









screen.exitonclick()



