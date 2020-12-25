import tkinter
import tkMessageBox

top = Tkinter.Tk()
def hello():
   tkMessageBox.showinfo("New Box")

B1 = Tkinter.Button(top, text = "Hello Box", command = hello)
B1.pack()

top.mainloop()