from tkinter import *
import tkinter as tks
from tkinter import IntVar

tk = Tk()
tk.geometry('500x500')
tk.title('Drop Down Menu')


main_menu = tks.Menu()
file = Menu(main_menu, tearoff = False)
main_menu.add_cascade(label= "File", menu = file)

file.add_command(label ="New", compound = tks.LEFT,  accelerator = "Ctrl +N")
file.add_command(label ="Open", compound = tks.LEFT,  accelerator = "Ctrl +O")
file.add_command(label ="Save", compound = tks.LEFT,  accelerator = "Ctrl +S")
file.add_command(label ="Save as", compound = tks.LEFT,  accelerator = "Ctrl +NS")
file.add_command(label ="Exit", compound = tks.LEFT,  accelerator = "Ctrl +Esc")



tk.config(menu=main_menu)

tk.mainloop()
