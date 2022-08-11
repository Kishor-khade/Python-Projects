from random import choice
from tkinter import *
import pandas as pd


window = Tk()
window.title("Hello")
window.config(padx=40, pady=40, bg='#b4c7dc')


data = pd.read_csv('Spread-Sheet.csv')
to_learn = data.to_dict(orient='records')
word = ''


def next_card():
    global word ,flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card, image=card_front)
    word = choice(to_learn)
    canvas.itemconfig(card_word, text=f"{word['Hindi']}")
    flip_timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(word)
    next_card()


def flip_card():
    canvas.itemconfig(card, image=card_back)
    English_word = word['English']
    canvas.itemconfig(card_word, text=f"{English_word}")
    canvas.itemconfig(card_lang, text="English")


card_front = PhotoImage(file='card_bg.png')
card_back = PhotoImage(file='card.png')

canvas = Canvas(width=800, height=500, bg='#b4c7dc', highlightthickness=0)
card = canvas.create_image(400, 350, image=card_front)
card_lang = canvas.create_text(400, 180, text='Hindi', font=('Monospace', 30, 'normal'))
card_word = canvas.create_text(400, 250, text='word', font=('Cursive', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2, pady=40)


cross_mark = PhotoImage(file='cross.png')
unKnown_button = Button(image=cross_mark, bg='#b4c7dc', highlightthickness=0, command=next_card)
unKnown_button.grid(row=1, column=0, pady=20)


tick_mark = PhotoImage(file='tick.png')
Known_button = Button(image=tick_mark, bg='#b4c7dc', highlightthickness=0, command=is_known)
Known_button.grid(row=1, column=1, pady=20)


flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()