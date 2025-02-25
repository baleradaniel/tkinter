from tkinter import *
i = Tk()
i.title('Programa Financeiro')
i.geometry('980x720+250+30')

lb1 = Label(i, text='Login', bg='yellow')
# componente .grid serve também para posicionar utilizando indicativo de linha(row) e coluna(column)
lb1.place(x=750, y=120)

lb2 = Label(i, text='Senha', bg='red')
lb2.place(x=750, y=320)

ed1 = Entry(i)
ed1.place(x=700, y=100)

ed2 = Entry(i)
ed2.place(x=700, y=300)

bt1 = Button(i, text='Login')
bt1.place(x=480, y=500)

i.mainloop()