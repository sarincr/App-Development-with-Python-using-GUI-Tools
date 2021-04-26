from tkinter import *
import tkinter as tks
from tkinter import IntVar

tk = Tk()
tk.geometry('500x500')
tk.title('Drop Down Menu')


main_menu = tks.Menu()
file = Menu(main_menu, tearoff = False)
main_menu.add_cascade(label= "File", menu = file)

tk.config(menu=main_menu)

tk.mainloop()
