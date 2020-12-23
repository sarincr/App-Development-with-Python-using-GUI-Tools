from tkinter import *

window = Tk()

window.title("Form Submission")

window.geometry('350x350')

label = Label(window, text="Good Morning")

label.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

def clicked():

    label.configure(text="You have submitted")

button = Button(window, text="Click Here", command=clicked)

button.grid(column=2, row=0)

window.mainloop()