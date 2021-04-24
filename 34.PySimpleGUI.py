import PySimpleGUI as PySG
lay = [  [PySG.Text("What's your name?")],
            [PySG.Input()],
            [PySG.Button('Ok')] ]


wd = PySG.Window('Python Simple GUI', lay)      
                                                
event, values = wd.read() 

print('Hello', values[0])

wd.close()      
