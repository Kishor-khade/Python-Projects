import turtle
import pandas as pd

"""
processing data: 
step1:
    Data was downloaded from : 
        1) https://www.downloadexcelfiles.com/in_en/download-excel-file-list-indian-states
        2) https://www.downloadexcelfiles.com/in_en/download-excel-file-list-union-territories-india

    And then processed the state and ut name into single csv file named Total_states 

step2:
    The below program was compiled and the locations of all states/ut's are noted 
    and saved in csv file named New_csv.
    -----------------------------------------------------------------
    data = pd.DataFrame()
    data['x'] ,data['y'] = 0, 0


    def get_mouse_click(x, y):
        data.loc[0] = x, y
        data.to_csv('New_csv.csv', mode='a', index=None, header=None)

    turtle.onscreenclick(get_mouse_click)
    turtle.mainloop()
    -----------------------------------------------------------------

step3:
    Then both the files merged in to single file 

"""


scr = turtle.Screen()
scr.title("Indian States")
scr.setup(width=820, height=950)


image = "Indian-Outline.gif"
scr.addshape(image)
turtle.shape(image)


data = pd.read_csv('Indian_states.csv', index_col='S.No')

all_states = data.States.to_list()
guessed_states = []
remaining_states = all_states


while True:
    guess = scr.textinput(title=f'{len(guessed_states)}/36  Identify States',
                          prompt="What's another the state/UT name?").title()

    if guess == 'Exit':
        for state in remaining_states:
            new_turtle = turtle.Turtle()
            new_turtle.color('red')
            new_turtle.hideturtle()
            new_turtle.penup()
            state_data = data[data.States == state]
            new_turtle.goto(int(state_data.x),
                            int(state_data.y))
            new_turtle.write(f"{state}")
        break

    if guess in all_states:
        guessed_states.append(guess)
        new_turtle = turtle.Turtle()
        new_turtle.color('black')
        new_turtle.penup()
        new_turtle.hideturtle()
        state_data = data[data.States == guess]
        new_turtle.goto(int(state_data.x),
                        int(state_data.y))
        new_turtle.write(f"{guess}")
        remaining_states.remove(guess)


scr.exitonclick()
