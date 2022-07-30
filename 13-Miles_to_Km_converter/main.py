from tkinter import *

from click import command

window = Tk()
window.title("Miles to KiloMeter Comverter")
window.config(padx=25, pady=20)

#                         input     miles(label)
# is-equal-to(label)     0(label)     km(label)
#                     calculate(btn)

def btn_clicked():
    mile = int(mile_entry.get())
    km_value.config(text=f"{mile*1.609}")


mile_entry = Entry(width=7)
mile_entry.grid(column=1, row=0)


mile = Label(text="Miles")
mile.grid(column=2, row=0)


equal_to = Label(text="Is Equal to ")
equal_to.grid(column=0, row=1)


km_value = Label(text="0")
km_value.grid(column=1, row=1)


km = Label(text="Km")
km.grid(column=2, row=1)


btn = Button(text="Calculate", command = btn_clicked)
btn.grid(column=1, row=2)





window.mainloop()