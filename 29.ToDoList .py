from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.geometry('500x450+500+200')
tk.title('PythonGuides')
tk.config(bg='#223441')
tk.resizable(width=False, height=False)

fr = Frame(tk)
fr.pack(pady=10)

lb = Listbox(fr,activestyle="none",)
lb.pack(side=LEFT, fill=BOTH)

lst = [1 ,2,3,5,4,6,6,3,2]

for x in lst:
    lb.insert(END, x)

scr = Scrollbar(fr)
scr.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=scr.set)
scr.config(command=lb.yview)

entr = Entry(tk)
entr.pack(pady=20)

btnfr = Frame(tk)
btnfr.pack(pady=20)

def addbtnTSK():
    X = entr.get()
    if X != "":
        lb.insert(END, X)
        entr.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


addbtn = Button(btnfr, text='Add Task', command=addbtnTSK)
addbtn.pack(fill=BOTH, expand=True, side=LEFT)

def delTSK():
    lb.delete(ANCHOR)

delbtn = Button(btnfr, text='Delete Task', command= delTSK)
delbtn.pack(fill=BOTH, expand=True, side=LEFT)

tk.mainloop()