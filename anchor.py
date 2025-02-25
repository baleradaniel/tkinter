from tkinter import *
i = Tk()
i.title('Programa Financeiro')
i.geometry('980x720+250+30')

lb1 = Label(i, text='Label 1', bg='yellow')
lb1.place(x=230, y=200)

lb2 = Label(i, text='Label 2', bg='pink')
lb2.place(x=230, y=200)

lb3 = Label(i, text='Label 3', bg='lightgreen')
lb3.place(x=230, y=200)

lb4 = Label(i, text='Label 4', bg='red')
lb4.place(x=230, y=200)

# codigo abaixo posiciona cada label em lugares diferentes
# após testar comente a linha do lb1 até o lb4

lb1.pack(side=LEFT)
lb2.pack(side='left')
lb3.pack(anchor='w') # sempre que não utilizo a opção side, ele sempre será topo
# lb4.pack(anchor='') # sempre que não utilizo a opção side, ele sempre será topo

# lb4.pack(side=BOTTOM, anchor='sw')

lb4.pack(anchor='e')

i.mainloop()