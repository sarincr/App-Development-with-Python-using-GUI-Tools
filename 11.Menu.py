from tkinter import *

top = Tk()

menubtn =  Menubutton ( top, text = "Select a Option", relief = RAISED )
menubtn.grid()
menubtn.menu  =  Menu ( menubtn, tearoff = 0 )
menubtn["menu"]  =  menubtn.menu
    
x  = IntVar()
y = IntVar()

menubtn.menu.add_checkbutton ( label = "Yes",
                          variable = x )
menubtn.menu.add_checkbutton ( label = "No",
                          variable = y )

menubtn.pack()
top.mainloop()