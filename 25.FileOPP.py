from tkinter import *
from tkinter import filedialog
base = Tk()

base.geometry('200*200')

def file_opener():
   input = filedialog.askopenfile(initialdir="/")
   print(input)
   for i in input:
      print(i)

btn = Button(base, text ='Select a .txt/.csv file', command = lambda:file_opener())
btn.pack()
mainloop()
