from tkinter import *

tk = Tk()
tk.geometry('500x500')
tk.title('Drop Down Menu')


choice = [ "Yes", "No" , "May Be" ]

x = StringVar()
x.set( "Select an option" )

def submit():
    lb.config( text = x.get() )



menu_input = OptionMenu( tk, x , *choice )
menu_input.pack()

btn = Button( tk, text = "Submit" , command = submit ).pack()


lb = Label( tk , text = " " )
lb.pack()

tk.mainloop()
