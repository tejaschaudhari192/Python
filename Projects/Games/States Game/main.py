import time
import turtle
import pandas as pd

# ------------------------------Path------------------------------#

csv_file_path = "C:/programming/Python/Projects/Games/States Game/states_data.csv"
india_map = "C:/programming/Python/Projects/Games/States Game/india.gif"
exit_key = 'x'.title()

# ------------------------------Dataset------------------------------#

state_data = pd.read_csv(csv_file_path)
state_list = state_data["state"].to_list()

# ------------------------------GUI------------------------------#

window = turtle.Screen()
window.title("India State Game")
window.addshape(india_map)
turtle.shape(india_map)


def ScoreBoard():
    window.title(f"India State Game\t\t\t\t{len(guessed)}/29 guessed")


# ------------------------------Game Control------------------------------#

guessed = []
game_over = False
while game_over is False:

    # exceptional handling for blank input
    try:
        user_state = window.textinput(
            title="Enter State or x to exit", prompt=""
        ).title()
    except AttributeError:
        continue
    else:
        pass

    if user_state == exit_key:
        game_over = True

    if user_state in state_list:
        row = state_data[state_data.state == user_state]
        x = int(row.x)
        y = int(row.y)

        writer = turtle.Turtle()
        # writer.penup()
        writer.hideturtle()
        writer.clear()
        writer.goto(x, y)
        writer.clear()
        writer.write(user_state)
        guessed.append(user_state)
        ScoreBoard()

    if len(guessed) >= 29:
        game_over = True
        window.title(f"India State Game\t\t\t\tYou Won")

learn = [state for state in state_list if state not in guessed]
# print(learn)
states_learn = pd.DataFrame(learn)
states_learn.to_csv("states_to_learn.csv")

window.exitonclick()

# exit(0)

# def coor(x, y):
#     print(f"{x},{y}")
# turtle.onscreenclick(coor)

# window.mainloop()
