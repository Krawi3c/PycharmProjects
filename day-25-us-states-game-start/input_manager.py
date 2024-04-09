from turtle import Turtle
import pandas

class InputManager:

    def __init__(self):
        self.states_data = []
        data = pandas.read_csv("50_states.csv")
        self.states_names = data["state"].to_list()
        states_position_x = data["x"].to_list()
        states_position_y = data["y"].to_list()
        for state in range(len(self.states_names)):
            self.states_data.append([self.states_names[state], states_position_x[state], states_position_y[state]])

    def create_state(self, name):
        for state in self.states_data:
            if state[0] == name:
                state_positions = (state[1], state[2])
        state = Turtle()
        state.penup()
        state.hideturtle()
        state.goto(state_positions)
        state.write(name, font=("Verdana", 8, "normal"))

    def answer_check(self, answer):
        if answer in self.states_names:
            self.create_state(answer)
            return True

