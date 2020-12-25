from tkinter import *

tk = Tk()
scrollbar = Scrollbar(tk)
scrollbar.pack( side = RIGHT, fill = Y )

lst = Listbox(tk, yscrollcommand = scrollbar.set )
for line in range(100):
   lst.insert(END, "Option No = " + str(line))

lst.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = lst.yview )

mainloop()