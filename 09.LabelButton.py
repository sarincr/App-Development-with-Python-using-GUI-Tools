from tkinter import *

window = Tk()
def clicked():

    ax.configure(text=" You have clicked the button")

window.title("Name of the Window")


window.geometry('350x200')

ax = Label(window, text="Hellow User")

ax.grid(column=0, row=0)

button = Button(window, text="Submit", command=clicked)

button.grid(column=1, row=0)

window.mainloop()