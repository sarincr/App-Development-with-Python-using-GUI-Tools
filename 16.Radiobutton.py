from tkinter import *

from tkinter.ttk import *

tks = Tk()

tks.title("Radio Button")

tks.geometry('350x200')

b1 = Radiobutton(tks,text='Yes', value=1)

b2 = Radiobutton(tks,text='No', value=2)

b3 = Radiobutton(tks,text='May be', value=3)

b1.grid(column=0, row=0)

b2.grid(column=1, row=0)

b3.grid(column=2, row=0)

tks.mainloop()