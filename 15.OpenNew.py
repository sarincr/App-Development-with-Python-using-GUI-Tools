from tkinter import *  
      
tks = Tk()  
tks.geometry("350x200")  
def Box(): 
    new =  Toplevel(tks)
    new.mainloop()  
      
Button = Button(tks, text = "Click Here", command = Box)  
      
Button.place(x=75,y=50)  
      
tks.mainloop()  