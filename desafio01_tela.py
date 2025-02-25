from tkinter import *
i = Tk()
i.title('Programa Financeiro')
i.geometry('980x720+250+30')

lb1 = Label(i, text='Login', bg='yellow')
lb1.place(x=1420, y=220)

lb2 = Label(i, text='Senha', bg='red')
lb2.place(x=1420, y=420)

ed1 = Entry(i, width=50)
ed1.place(x=1300, y=200)

ed2 = Entry(i, width=50)
ed2.place(x=1300, y=400)

bt1 = Button(i, text='Login', width=40)
bt1.place(x=850, y=700)

i.mainloop()