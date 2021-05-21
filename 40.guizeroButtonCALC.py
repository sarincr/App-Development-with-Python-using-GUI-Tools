from guizero import App, Text, Box, PushButton
def do_nothing():
    return 0

app = App(title="My app", height=130, width=110, layout="grid")
box = Box(app, layout="grid", grid=[1,0])
button1 = PushButton(box, command=do_nothing, text="1", grid=[0,0])
button2 = PushButton(box, command=do_nothing, text="2", grid=[1,0])
button3 = PushButton(box, command=do_nothing, text="3", grid=[2,0])
button4 = PushButton(box, command=do_nothing, text="4", grid=[0,1])
button5 = PushButton(box, command=do_nothing, text="5", grid=[1,1])
button6 = PushButton(box, command=do_nothing, text="6", grid=[2,1])
button7 = PushButton(box, command=do_nothing, text="6", grid=[0,2])
button8 = PushButton(box, command=do_nothing, text="6", grid=[1,2])
button9 = PushButton(box, command=do_nothing, text="6", grid=[2,2])
app.display()

