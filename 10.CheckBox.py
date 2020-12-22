from tkinter import *   
top = Tk()  
top.geometry("200x200")  
x = IntVar() 
y = IntVar() 
z = IntVar()  
b1 = Checkbutton(top, 
                 text = "Yes", 
                 variable = x, 
                 onvalue = 1, 
                 offvalue = 0, 
                 height = 2, 
                 width = 10) 
b2 = Checkbutton(top, 
                 text = "No", 
                 variable = y, 
                 onvalue = 1, 
                 offvalue = 0, 
                 height = 2, 
                 width = 10)  
b3 = Checkbutton(top, 
                 text = "NA", 
                 variable = z, 
                 onvalue = 1, 
                 offvalue = 0, 
                 height = 2, 
                 width = 10) 
b1.pack()  
b2.pack()  
b3.pack() 
top.mainloop()  