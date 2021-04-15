import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root)
canvas1.pack()

def getCSV ():
    global df
    location = filedialog.askopenfilename()
    df = pd.read_csv (location)
    print (df)
    
btn = tk.Button(text=" Import CSV", command=getCSV)
canvas1.create_window(150, 150, window=btn)

root.mainloop()
