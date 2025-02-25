from tkinter import *

def bt_soma():
    # codigo abaixo é para validar a entrada apenas de numeros
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        #se os valores nao forem numericos imprime a mensagem abaixo:
        lb["text"] = num1 + num2
        lb['bg'] = '#00FA9A'
    else:
        lb['text'] = 'Valores são invalidos'
        lb['bg'] = 'red'

def bt_sub():
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 - num2
        lb['bg'] = '#00FA9A'
    else:
        lb['text'] = 'Valores são invalidos'
        lb['bg'] = 'red'

def bt_mult():
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 * num2
        lb['bg'] = '#00FA9A'

    else:
        lb['text'] = 'Valores são invalidos'
        lb['bg'] = 'red'
        

def bt_divi():
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):    
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 / num2
        lb['bg'] = '#00FA9A'
    
    else:
        lb['text'] = 'Valores são invalidos'
        lb['bg'] = 'red'

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb = Label(i, text="0")
lb.place(x=230, y=200)

lb = Label(i, text="Daniel Balera")
lb.place(x=230, y=500)

bt = Button(i, width='20', text='Somar', command=bt_soma)
bt.place(x=230,y=230)

bt = Button(i, width='20', text='Subtrair', command=bt_sub)
bt.place(x=230,y=250)

bt = Button(i, width='20', text='Multiplicar', command=bt_mult)
bt.place(x=230,y=270)

bt = Button(i, width='20', text='Dividir', command=bt_divi)
bt.place(x=230,y=290)

ed1 = Entry(i)
ed1.place(x=230, y=150)

ed2 = Entry(i)
ed2.place(x=230, y=180)

i.mainloop()
