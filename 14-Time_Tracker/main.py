from math import floor
from tkinter import *


#--------------------------------------- CONSTANTS -------------------------------------#
SHORT_BREAK = 5
LONG_BREAK = 20
WORK_TIME = 25
reps = 0
timer = None


#------------------------------------- TIMER RESET --------------------------------------#
def timer_reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    heading.config(text='   Timer    ', fg='white')
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text='')


#------------------------------------ TIMER MEVCHANISM ----------------------------------#
def start_timer():
    global reps
    if reps % 2 == 0:
        heading.config(text='Working Time', fg='green',
                       font=('Courier', 50, 'normal'))
        count_down(WORK_TIME * 60)
    elif reps == 7:
        heading.config(text='   Break    ', fg='#C85C5C',
                       font=('Series', 50, 'bold'))
        count_down(LONG_BREAK * 60)
        reps = -1
    else:
        heading.config(text='   Break    ', fg='#e2979c')
        count_down(SHORT_BREAK*60)
    reps += 1


#---------------------------------- COUNTDOWN MECHANISM ---------------------------------#
def count_down(count):
    global reps
    if count >= 0:
        count_min = floor(count/60)
        count_sec = count % 60
        count_min = f'0{count_min}' if count_min < 10 else f'{count_min}'
        count_sec = f'0{count_sec}' if (count_sec) < 10 else f'{count_sec}'
        print(count_min, count_sec)
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        if (reps % 2 != 0):
            check_mark.config(text='✔'*floor(reps/2 + 1))
        start_timer()


#---------------------------------------- UI SETUP ---------------------------------------#
window = Tk()
window.title("Time Tracker")
window.config(padx=20, pady=20, bg='black')


heading = Label(text='   Timer    ', bg='black', fg='white',
                font=('Courier', 50, 'normal'))
heading.grid(row=0, column=1)


canvas = Canvas(width=400, height=200, bg='black', highlightthickness=0)
timer_text = canvas.create_text(200, 100, text='00:00', fill='red', 
                                font=('Serif', 70, 'normal'))
canvas.grid(row=1, column=1, padx=5, pady=5)


strt_btn = Button(text='Start', bg='black', fg='#F5EEDC', command=start_timer, 
                  font=('serif', 15, 'normal'), highlightthickness=0)
strt_btn.grid(row=2, column=0, padx=10, pady=10)


reset_btn = Button(text='Reset', bg='black', fg='#F5EEDC', command=timer_reset, 
                   font=('serif', 15, 'normal'), highlightthickness=0)
reset_btn.grid(row=2, column=2, padx=10, pady=10)


# check_mark = Label(text='✅', bg='black', fg='green', font=('Courier', 30, 'bold'))
# check_mark = Label(text='☑', bg='black', fg='green', font=('Courier', 30, 'bold'))
check_mark = Label(text='', bg='black', fg='green',
                   font=('Courier', 30, 'bold'))
check_mark.grid(row=3, column=1, pady=20)


window.mainloop()
