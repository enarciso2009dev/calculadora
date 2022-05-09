from tkinter import *
from tkinter import messagebox
from util.numeros import Numeros


class Calculadora:



    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("300x500")
        self.janela.title('Calculadora de Horas')
        num = Numeros()


        #display
        self.entrada1 = Entry(self.janela, bd=3)
        self.entrada1.place(x=20, y=40, w=260, h=30)

        self.resultado = Entry(self.janela, bd=3)
        self.resultado.place(x=20, y=70, w=260, h=30)

        self.botaoon = Button(self.janela, text='C')
        self.botaoon.place(x=208, y = 110, w=30, h=30)


        #botoẽs converte numero para horas
        self.botaoh = Button(self.janela,text = 'H', command = self.exibeh) #command=lambda: self.random_number(8))
        self.botaoh.place(x=20, y=150, w=70, h=40)

        # converte horas para minutos
        botaom = Button(self.janela, text = 'M', command = self.exibem)
        botaom.place(x=113, y=150, w=70, h=40)
        # converte para horas centesimais)
        botaod = Button(self.janela, text = 'D', command = self.exibed)
        botaod.place(x=208, y=150, w=70, h=40)
        # botoes divisao
        botaodiv = Button(self.janela, text = '/')
        botaodiv.place(x=218, y=230, w=60, h=30)
        # botoes multiplicacao
        botaox = Button(self.janela, text = 'X')
        botaox.place(x=218, y=280, w=60, h=30)
        # botoes subtracao
        botaos = Button(self.janela, text = '-'+'-')
        botaos.place(x=218, y=330, w=60, h=30)
        # botoes soma
        botaoso = Button(self.janela, text = '+')
        botaoso.place(x=218, y=380, w=60, h=30)
        # botoes igual
        botaoi = Button(self.janela, text = '=')
        botaoi.place(x=158, y=430, w=120, h=30)
        # botoes numeros 7 8 9
        self.botao7 = Button(self.janela, text = '7', command = self.mostra7)
        self.botao7.place(x=20, y=230, w=60, h=30)
        #botao7.entrada1(text)

        botao8 = Button(self.janela, text = '8', command = self.mostra8)
        botao8.place(x=86, y=230, w=60, h=30)

        botao9 = Button(self.janela, text = '9', command = self.mostra9)
        botao9.place(x=152, y=230, w=60, h=30)
        # botoes 4 5 6
        botao4 = Button(self.janela, text = '4', command = self.mostra4)
        botao4.place(x=20, y=280, w=60, h=30)

        botao5 = Button(self.janela, text = '5', command = self.mostra5)
        botao5.place(x=86, y=280, w=60, h=30)

        botao6 = Button(self.janela, text = '6', command = self.mostra6)
        botao6.place(x=152, y=280, w=60, h=30)
        # botoes 1 2 3
        botao1 = Button(self.janela, text = '1', command = self.mostra1)
        botao1.place(x=20, y=330, w=60, h=30)

        botao2 = Button(self.janela, text = '2', command = self.mostra2)
        botao2.place(x=86, y=330, w=60, h=30)

        botao3 = Button(self.janela, text = '3', command = self.mostra3)
        botao3.place(x=152, y=330, w=60, h=30)
        #botoes : 0 ,
        botao2p = Button(self.janela, text = ':', command = self.mostra2p)
        botao2p.place(x=20, y=380, w=60, h=30)

        botao0 = Button(self.janela, text = '0', command = self.mostra0)
        botao0.place(x=86, y=380, w=60, h=30)

        botaov = Button(self.janela, text = ',', command = self.mostrav)
        botaov.place(x=152, y=380, w=60, h=30)
        #botoes : 00

        botao00 = Button(self.janela, text = '00', command = self.mostra00)
        botao00.place(x=86, y=430, w=60, h=30)

        botaop = Button(self.janela, text = '.', command = self.mostrap)
        botaop.place(x=20, y=430, w=60, h=30)
        v = StringVar

        mainloop()
#NUMEROS
    def mostra9(self):
        self.num = 9
        return self.entrada1.insert(0, self.num)
    def mostra8(self):
        self.num = 8
        return self.entrada1.insert(0, self.num)
    def mostra7(self):
        self.num = 7
        return self.entrada1.insert(0, self.num)
    def mostra6(self):
        self.num = 6
        return self.entrada1.insert(0, self.num)
    def mostra5(self):
        self.num = 5
        return self.entrada1.insert(0, self.num)
    def mostra4(self):
        self.num = 4
        return self.entrada1.insert(0, self.num)
    def mostra3(self):
        self.num = 3
        return self.entrada1.insert(0, self.num)
    def mostra2(self):
        self.num = 2
        return self.entrada1.insert(0, self.num)
    def mostra1(self):
        self.num = 1
        return self.entrada1.insert(0, self.num)
    def mostra0(self):
        self.num = 0
        return self.entrada1.insert(0, self.num)
    def mostra00(self):
        self.num = 00
        return self.entrada1.insert(0, self.num)
    def mostrap(self):
        self.num = '.'
        return self.entrada1.insert(0, self.num)
    def mostra2p(self):
        self.num = ':'
        return self.entrada1.insert(0, self.num)
    def mostrav(self):
        self.num = ','
        return self.entrada1.insert(0, self.num)


    def exibeh(self):
        self.valor = int(self.entrada1.get())
        self.result = self.valor / 60
        print(f'agora esta certo {self.result}')
        return self.resultado.insert(0,self.result)

    def exibem(self):
        self.valor = int(self.entrada1.get())
        self.result = self.valor * 60
        print(f'agora esta certo {self.result}')
        return self.resultado.insert(0,self.result)

    def exibed(self):
        self.valor = str(self.entrada1.get())
        self.min = str(self.valor.split(':'))
        self.tmin = (self.min[1])
        self.res = int(self.tmin / (6 / 10))
        return self.resultado.insert(0, self.res)




calc = Calculadora()
