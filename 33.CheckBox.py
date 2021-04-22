from tkinter import *
from tkinter import IntVar

tk = Tk()
tk.geometry('500x500')
tk.title('Drop Down Menu')




lab = Label(tk, text="")
lab.pack()



def Check_Funct():
    if (X1.get() == 1) & (X2.get() == 0):
        lab.config(text='Item 1 selected ')
    elif (X1.get() == 0) & (X2.get() == 1):
        lab.config(text='Item 0 selected ')
    elif (X1.get() == 0) & (X2.get() == 0):
        lab.config(text='Not selected anything')
    else:
        lab.config(text='Item 1 and 2 Selected ')




X1 = IntVar()
X2 = IntVar()
check1 = Checkbutton(tk, text='Item 1',variable=X1, onvalue=1, offvalue=0, command=Check_Funct)
check1.pack()
check2 = Checkbutton(tk, text='C++',variable=X2, onvalue=1, offvalue=0, command=Check_Funct)
check2.pack()



tk.mainloop()
