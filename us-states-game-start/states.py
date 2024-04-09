import pandas
from turtle import Turtle

class States:

    guessed = 0

    def __init__(self):
        data = pandas.read_csv("50_states.csv")
        self.states_names = data["state"].to_list()
        self.state_x = data["x"].to_list()
        self.state_y = data["y"].to_list()
        self.total = len(self.states_names)

    def update_title(self):
        self.title = f"{self.guessed}/{self.total} States Correct"

    def create_state(self, name):
        for state in self.states_names:
            if state == name:
                self.guessed+=1
                index = self.states_names.index(state)
                self.states_names.remove(state)
                state = Turtle()
                state.speed("fastest")
                state.hideturtle()
                state.penup()
                state.goto(self.state_x[index], self.state_y[index])
                state.write(name)
                self.update_title()
                return self.title

    def exit(self):
        to_learn = pandas.DataFrame(self.states_names)
        to_learn.to_csv("states_to_learn.csv")
