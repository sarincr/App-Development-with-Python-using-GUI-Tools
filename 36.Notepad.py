from tkinter import *
import tkinter as tks
from tkinter import IntVar

tk = Tk()
tk.geometry('500x500')
tk.title('Notepad')


main_menu = tks.Menu()
file = Menu(main_menu, tearoff = False)
edit = Menu(main_menu, tearoff = False)
view = Menu(main_menu, tearoff = False)
theme = Menu(main_menu, tearoff = False)
main_menu.add_cascade(label= "File", menu = file)
main_menu.add_cascade(label= "Edit", menu = edit)
main_menu.add_cascade(label= "View", menu = view)
main_menu.add_cascade(label= "Theme", menu = theme)

view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=False, compound=tks.LEFT)
view.add_checkbutton(label="Status Bar", onvalue=True, offvalue=False, compound=tks.LEFT)


file.add_command(label ="New", compound = tks.LEFT,  accelerator = "Ctrl +N")
file.add_command(label ="Open", compound = tks.LEFT,  accelerator = "Ctrl +O")
file.add_command(label ="Save", compound = tks.LEFT,  accelerator = "Ctrl +S")
file.add_command(label ="Save as", compound = tks.LEFT,  accelerator = "Ctrl +NS")
file.add_command(label ="Exit", compound = tks.LEFT,  accelerator = "Ctrl +Esc")


edit.add_command (label = 'Copy' ,  compound = tks.LEFT, accelerator = 'ctrl+C') 
edit.add_command (label = 'Paste' , compound = tks.LEFT, accelerator = 'ctrl+V')
edit.add_command (label = 'Cut' , compound = tks.LEFT, accelerator = 'ctrl+X')
edit.add_command (label = 'Clear' ,  compound = tks.LEFT, accelerator = 'ctrl+alt+x')
edit.add_command (label = 'Find' ,  compound = tks.LEFT, accelerator = 'ctrl+F')



color_dict = {

    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')

}

count = 0
for i in color_dict:
    theme.add_radiobutton(label = i , compound = tks.LEFT)
    count +=1



tk.config(menu=main_menu)

tk.mainloop()
