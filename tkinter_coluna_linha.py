from tkinter import *
i = Tk()
i.title('Programa Financeiro')
i.geometry('980x720+250+30')

# lb1 = Label(i, text='Login', bg='yellow')
# # componente .grid serve também para posicionar utilizando indicativo de linha(row) e coluna(column)
# lb1.grid(row=1, column=1)

# lb2 = Label(i, text='Senha', bg='red')
# lb2.grid(row=1, column=1)

# ed1 = Entry(i)
# ed1.grid(row=1, column=1)

# ed2 = Entry(i)
# ed2.grid(row=1,column=1)

# bt1 = Button(i, text='Login')
# bt1.grid(row=1, column=1)

# codigo abaixo faz corrções das posições das labels, caixa de texto e botao

lb1 = Label(i, text='Login', bg='yellow')
lb1.grid(row=1, column=1)

lb2 = Label(i, text='Senha', bg='red')
lb2.grid(row=2, column=1)

ed1 = Entry(i)
ed1.grid(row=1,column=2)

ed2 = Entry(i)
ed2.grid(row=2,column=2)

bt1 = Button(i, text='Login')
bt1.grid(row=3, column=1)
i.mainloop()