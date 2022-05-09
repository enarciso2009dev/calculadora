import colorsys
from tkinter import *
import math
from util.calculo import somar, subtrair, adicnot, multiplicar, dividir, percent

root =Tk()
class App():
    def __init__(self):
        self.root = root
        self.config()
        self.calculadora()
        root.mainloop()
    def config(self):
        self.root.title("Calculadora Horas")
        self.root.geometry("350x350")
        self.root.configure(bg='#F8F8FF')
        self.root.resizable(False, False)
    def calculadora(self):
        self.lbl1 = Label(text='Hora:', bg='#F8F8FF')
        self.lbl1.place(x=50, y=10)
        self.numero1 = StringVar()
        self.lbl1_enty = Entry(textvariable=self.numero1)
        self.lbl1_enty.place(x=100, y=10)
        self.lbl2 = Label(text='Hora2:', bg='#F8F8FF')
        self.lbl2.place(x=50, y=50)
        self.numero2 = StringVar()
        self.lbl2_enty = Entry(textvariable=self.numero2)
        self.lbl2_enty.place(x=100, y=50)
      # Resultado
        self.lbl3 = Label(text='Resultado:', bg='#F8F8FF')
        self.lbl3.place(x=50, y=90)
        self.resultado = StringVar()
        self.l_resultado = Label(textvariable=self.resultado, font=("Helvetica", '18'), bg='#F8F8FF')
        self.l_resultado.place(x=140, y=90)


       #Butão
        self.btn1 = Button(text='+', bg='#E0FFFF',command=self.somar)
        self.btn1.place(x=50, y=150, w=50, h=50)
        self.btn2 = Button(text='-', bg='#E0FFFF',command=self.sub)
        self.btn2.place(x=117, y=150, w=50, h=50)
        self.btn3 = Button(text='X', bg='#E0FFFF', command=self.multip)
        self.btn3.place(x=183, y=150, w=50, h=50)
        self.btn4 = Button(text='/', bg='#E0FFFF', command=self.divis)
        self.btn4.place(x=250, y=150, w=50, h=50)

        self.btn5 = Button(text='Adic. Not', bg='#E0FFFF',command=self.adic)
        self.btn5.place(x=50, y= 220, w=114, h=50)

        self.btn6 = Button(text='%', bg='#E0FFFF', command=self.perc)
        self.btn6.place(x=183, y=220, w=114, h=50)

    def adic(self):
        num1 = self.numero1.get()
        numa = (num1.split(":"))
        hora1 = int(numa[0])
        hr1 = hora1
        min1 = int(numa[1])
        mm1 = min1
        adc = str(adicnot(hr1, mm1))
        hora = adc.split('.')
        rec = hora[0]
        hora1 = rec.split(':')
        hr = hora1[0]
        mm = hora1[1]

        result_conv = (f'{hr}:{mm}')
        self.resultado.set(result_conv)

    def somar(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        numa = (num1.split(":"))
        hora1 = int(numa[0])
        hr1 = hora1
        numb = (num2.split(":"))
        hora2 = int(numb[0])
        hr2 = hora2
        min1 = int(numa[1])
        mm1 = min1
        min2 = int(numb[1])
        mm2 = min2
        soma = str(somar(hr1, mm1, hr2, mm2))
        self.resultado.set(soma)

    def sub(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        numa = (num1.split(":"))
        hora1 = int(numa[0])
        hr1 = hora1
        numb = (num2.split(":"))
        hora2 = int(numb[0])
        hr2 = hora2
        min1 = int(numa[1])
        mm1 = min1
        min2 = int(numb[1])
        mm2 = min2
        subr = str(subtrair(hr1, mm1, hr2, mm2))
        self.resultado.set(subr)

    def multip(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        numa = (num1.split(":"))
        hora1 = int(numa[0])
        hr1 = hora1
        mm = int(num2)
        min1 = int(numa[1])
        mm1 = min1
        mult = (multiplicar(hr1, mm1, mm))
        self.resultado.set(mult)

    def divis(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        numa = (num1.split(":"))
        hora1 = int(numa[0])
        hr1 = hora1
        mm = int(num2)
        min1 = int(numa[1])
        mm1 = min1
        div = (dividir(hr1, mm1, mm))
        self.resultado.set(div)

    def perc(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        numa = (num1.split(":"))
        hora1 = int(numa[0])
        hr1 = hora1
        mm = int(num2)
        min1 = int(numa[1])
        mm1 = min1
        per = (percent(hr1, mm1, mm))
        self.resultado.set(per)


App()
