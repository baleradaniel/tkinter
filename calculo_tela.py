from tkinter import *

def bt_soma():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 + num2
    
def bt_sub():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 - num2

def bt_mult():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 * num2

def bt_divi():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 / num2

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')
i["bg"] = "blue"

lb = Label(i, text="0")
lb.place(x=230, y=200)

lb = Label(i, text="Daniel Balera")
lb.place(x=230, y=500)

bt = Button(i, width='20', text='Somar', command=bt_soma)
bt.place(x=230,y=230)
bt["bg"] = "blue"

bt = Button(i, width='20', text='Subtrair', command=bt_sub)
bt.place(x=230,y=250)
bt["bg"] = "grey"

bt = Button(i, width='20', text='Multiplicar', command=bt_mult)
bt.place(x=230,y=270)

bt = Button(i, width='20', text='Dividir', command=bt_divi)
bt.place(x=230,y=290)

ed1 = Entry(i)
ed1.place(x=230, y=150)

ed2 = Entry(i)
ed2.place(x=230, y=180)

i.mainloop()
