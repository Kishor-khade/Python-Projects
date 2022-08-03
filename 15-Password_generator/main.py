from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip


#------------------------------ Password Generator ----------------------------#
def generate_password():
    """ Generate password and saves it in clipboard """
    password = []

    CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    NUMBERS = ['1', '2', '3', '3', '5', '6', '7', '8', '8', '9', '0']

    SYMBOLS = ['!', '@', '#', '$', '%', '&', '*', '_', '+', '-']

    no_characters = randint(8, 10)
    no_numbers = randint(2, 4)
    no_symbols = randint(2, 4)

    [password.append(choice(CHARACTERS)) for _ in range(no_characters)]
    [password.append(choice(NUMBERS)) for _ in range(no_numbers)]
    [password.append(choice(SYMBOLS)) for _ in range(no_symbols)]

    shuffle(password)
    password_input.insert(0, ''.join(password))

    pyperclip.copy(''.join(password))


#-------------------------------- Save password -------------------------------#
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if website == '':
        messagebox.showerror(title='Error', message='Please! Enter website')
        return None
    if username == '':
        messagebox.showerror(
            title='Error', message='Please! \nEnter mail or username')
        return None
    if password == '':
        messagebox.showerror(title='Error', message='Password was not entered')
        return None

    is_ok = messagebox.askokcancel(
        title='Details',
        message=f"The entered details are \n\n Website            : {website} \n\n Mail/Username  : {username} \n\n Password          : {password}"
    )
    if is_ok:
        with open('data.txt', 'a') as file:
            file.write(f"{website}  |  {username}  |  {password}\n")
        reset()
        messagebox.showinfo(title="Password Manager",
                            message='Details Saved successfully')


def reset():
    website_input.delete(first=0, last=END)
    username_input.delete(first=0, last=END)
    password_input.delete(first=0, last=END)


#---------------------------------- UI Setup ----------------------------------#
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg='#F5F5F5')

image = PhotoImage(file='image.png')
canvas = Canvas(width=200, height=220, bg='white', highlightthickness=0)
canvas.create_image(100, 110, image=image)
canvas.grid(column=1, row=0, padx=20, pady=20)


website_label = Label(text='Website : ', bg='#F5F5F5')
website_label.grid(column=0, row=1)
username_label = Label(text='Email / UserName : ', bg='#F5F5F5')
username_label.grid(column=0, row=2)
password_label = Label(text='Password : ', bg='#F5F5F5')
password_label.grid(column=0, row=3)


website_input = Entry(width=46)
website_input.grid(column=1, row=1, columnspan=2, pady=5)
website_input.focus()
username_input = Entry(width=46)
username_input.grid(column=1, row=2, columnspan=2, pady=5)
password_input = Entry(width=27)
password_input.grid(column=1, row=3, pady=5)


generate_pass_btn = Button(text='Generate Password', width=13,
                           bg='white', command=generate_password)
generate_pass_btn.grid(column=2, row=3)

add_button = Button(text='ADD', width=43, bg='white', command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=5)


window.mainloop()
