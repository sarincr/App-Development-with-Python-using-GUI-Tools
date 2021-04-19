from tkinter import *
from PyDictionary import PyDictionary

tk = Tk()
tk.geometry('500x500')
tk.title('Dictionary')

dictob = PyDictionary()

def dct():
    output = dictob.synlab(entrpck.get())
    print(output)
    synlab.config(text=output )

label = Label( tk, text="Enter the word", relief=RAISED )


entrpck = Entry(tk)
entrpck.pack()

btn = Button(tk, command=dct)
btn.pack()


synlab = Label(tk, text="", justify=LEFT, wraplength=150)
synlab.pack()

tk.mainloop()
