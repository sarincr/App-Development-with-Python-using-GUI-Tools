import tkinter as tk 
from tkinter  import * 

def sel():
   selection = "Data = " + str(var.get())
   label.config(text = selection)

tks = tk.Tk() 
var = DoubleVar()
sc = Scale( tks, variable = var )
sc.pack(anchor=CENTER)

bt = Button(tks, text="Get Scale Data", command=sel)
bt.pack(anchor=CENTER)

label = Label(tks)
label.pack()

tks.mainloop()