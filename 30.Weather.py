from tkinter import *

import requests
import json

tk = Tk()
tk.title('Find Weather')
tk.geometry("550x300")



def WethData():
    city = city_entry.get()
    state = state_entry.get()
    api_request = requests.get(f"https://api.hgbrasil.com/weather?key=d08c55d1&amp;city_name={city},{state};locale=en")
    api = json.loads(api_request.content)
    max = api['results']['forecast'][0]['max']
    min = api['results']['forecast'][0]['min']
    description = api['results']['description']
    WLab = Label(tk, text=f'Max temperature {max}°C  Min temperature {min}°C  {description}')
    WLab.grid(row=3, column=0)




lb = Label(tk, text='Check your location')
lb.grid(row=0, column=0)

pllab = Label(tk, text="Enter Place")
pllab.grid(row=1, column=0)

stlab= Label(tk, text='Enter State')
stlab.grid(row=2, column=0)

city_entry = Entry(tk, width=25, borderwidth=5)
city_entry.grid(row=1, column=1)

state_entry = Entry(tk, width=25, borderwidth=5)
state_entry.grid(row=2, column=1)

btn = Button(tk, text='search', command=WethData)
btn.grid(row=3, column=1)

tk.mainloop()