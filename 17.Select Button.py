from tkinter import *

from tkinter.ttk import *

tks = Tk()

tks.title("Enter Details")

X = IntVar()

b1 = Radiobutton(tks,text='Yes', value=1, variable=X)

b2 = Radiobutton(tks,text='No', value=2, variable=X)

b3 = Radiobutton(tks,text='May Be', value=3, variable=X)

def Submit():

   print(X.get())

Button = Button(tks, text="Submit", command=Submit)

b1.grid(column=0, row=0)

b2.grid(column=1, row=0)

b3.grid(column=2, row=0)

Button.grid(column=3, row=0)

tks.mainloop()
