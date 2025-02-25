from tkinter import *

# Criando uma função para clique no botão
def bt_click():
    # o label que usa propiedade TEXT receberá a mensagem "Trocou o texto"
    lb["text"] = "Trocou o texto"
    # esse print abaixo exibe o texto na tela do console
    print("O botão foi clicado!")

def bt_clicar():
    # esse print exibe o texto digitado na caixa de texto e exibe na label da tela
    print(ed.get())
    lb["text"]= ed.get()

# i (instanciar) recebe o objeto tk
i=Tk()

# gerar titulo na janela
i.title('Programa Financeiro')
i.geometry('980x720+250+30')
i["bg"]= "green"

# i.wm_iconbitmap('icone.ico')
lb = Label(i, text='Nome do usuario')
lb.place(x=100, y=100)

bt = Button(i, width="20", text='OK', command=bt_click)
bt.place(x=230, y=100)

#  botão que posiciona abaixo do botão OK
bt = Button(i, width="20", text='Capturar', command=bt_clicar)
bt.place(x=230, y=190)

# cria a caixa de texto
ed = Entry(i)
ed.place(x=230, y=150)

i.mainloop()