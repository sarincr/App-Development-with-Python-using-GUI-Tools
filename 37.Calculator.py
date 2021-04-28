import tkinter

tk = tkinter.Tk()
tk.title("Calculator")

Total = ""


result = tkinter.Label(tk, text="Result =")
result.grid(row=0, column=0, columnspan=4)

def add(X):
    global Total
    Total += X
    result.config(text=Total)
    print(X); 

def clean():
    global Total
    Total = ""
    result.config(text=Total)

def final_Calc():
    global Total
    final_result = ""
    if Total != "":
        try:
            final_result = eval(Total)
        except:
            final_result = "error"
            Total = ""
    result.config(text=final_result)

btn1 = tkinter.Button(tk, text="1", command=lambda: add("1"))
btn1.grid(row=1, column=0)

btn2 = tkinter.Button(tk, text="2", command=lambda: add("2"))
btn2.grid(row=1, column=1)

btn3 = tkinter.Button(tk, text="3",  command=lambda: add("3"))
btn3.grid(row=1, column=2)

btnDiv = tkinter.Button(tk, text="/",  command=lambda: add("/"))
btnDiv.grid(row=1, column=3)

btn4 = tkinter.Button(tk, text="4",  command=lambda: add("4"))
btn4.grid(row=2, column=0)

btn5 = tkinter.Button(tk, text="5",  command=lambda: add("5"))
btn5.grid(row=2, column=1)

btn6 = tkinter.Button(tk, text="6",  command=lambda: add("6"))
btn6.grid(row=2, column=2)

btnmul = tkinter.Button(tk, text="*",  command=lambda: add("*"))
btnmul.grid(row=2, column=3)


btn7 = tkinter.Button(tk, text="7",  command=lambda: add("7"))
btn7.grid(row=3, column=0)

btn8 = tkinter.Button(tk, text="8",  command=lambda: add("8"))
btn8.grid(row=3, column=1)

btn9 = tkinter.Button(tk, text="9",  command=lambda: add("9"))
btn9.grid(row=3, column=2)

btnadd = tkinter.Button(tk, text="+",  command=lambda: add("+"))
btnadd.grid(row=3, column=3)

btn0 = tkinter.Button(tk, text="0",  command=lambda: add("0"))
btn0.grid(row=4, column=0)

btnC = tkinter.Button(tk, text="C",  command=lambda: clean())
btnC.grid(row=4, column=1)

btnDOT = tkinter.Button(tk, text=".",  command=lambda: add("."))
btnDOT.grid(row=4, column=2)

btnSUB = tkinter.Button(tk, text="-",  command=lambda: add("-"))
btnSUB.grid(row=4, column=3)

btnEQ = tkinter.Button(tk, text="=", width=16,   command=lambda: final_Calc())
btnEQ.grid(row=5, column=0, columnspan=4)

tk.mainloop()
