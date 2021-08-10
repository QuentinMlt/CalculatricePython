import math
from tkinter import *


class Calc(object):
    def __init__(self,txtDisplay):
        self.total = 0
        self.current = ''
        self.ip_val = True
        self.check_sum = False
        self.op = ''
        self.result = False
        self.txtDisplay = txtDisplay

    def numberEnter(self, num):
        self.result = False
        first_num = self.txtDisplay.get()
        second_num = str(num)

        if self.ip_val:
            self.current = second_num
            self.ip_val = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(self.txtDisplay.get())

    def valid_function(self):
        if self.op == 'add':
            self.total += self.current
        elif self.op == 'sub':
            self.total -= self.current
        elif self.op == 'mul':
            self.total *= self.current
        elif self.op == 'div':
            self.total /= self.current
        elif self.op == 'mod':
            self.total %= self.current

        self.ip_val = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.ip_val = True
        self.check_sum = True
        self.op = op
        self.result = False

    # ------FONCTIONS BASIQUES AFFICHAGE

    def display(self, value):
        self.txtDisplay.delete(0, END)
        self.txtDisplay.insert(0, value)

    def clear_entry(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.ip_val = True

    def clear_all(self):
        self.clear_entry()
        self.total = 0

    # --------Constantes

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    # --------Calculs

    def carre(self):
        self.result = False
        self.current = float(self.txtDisplay.get()) * float(self.txtDisplay.get())
        self.display(self.current)

    def PM(self):
        self.result = False
        self.current = -(float(self.txtDisplay.get()))
        self.display(self.current)

    def sq_rt(self):
        self.result = False
        self.current = math.sqrt(float(self.txtDisplay.get()))
        self.display(self.current)

    def ln(self):
        self.result = False
        self.current = math.log(float(self.txtDisplay.get()))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log10(float(self.txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(self.txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(math.radians(float(self.txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(self.txtDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(self.txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(self.txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(self.txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(self.txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(self.txtDisplay.get())))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(self.txtDisplay.get()))
        self.display(self.current)

    def radians(self):
        self.result = False
        self.current = math.radians(float(self.txtDisplay.get()))
        self.display(self.current)
