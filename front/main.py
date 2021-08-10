from tkinter import *
from Class.Calc import Calc
from menuFunction.menu import Std, Sci, Exit


# CREATION APPLICATION
root = Tk()
root.title("Calculatrice Iskernel Python")
root.resizable(width=False, height=False)
root.geometry("378x308+0+0")
root.configure(background='black')


calc = Frame(root)
calc.grid()


# CONSOLE DE LA CALCULATRICE
txtDisplay = Entry(calc, font=('arial', 16, 'bold'), bd=20, bg='black', width=28, justify=RIGHT, fg='white')
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, '0')

# CREATION INSTANCE
res = Calc(txtDisplay)

# FRONT BOUTONS //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# BOUTONS PRINCIPAUX CALCULATRICE

numpad = '789456123'
i = 0
btn = []

for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=1, font=('arial', 16, 'bold'), bd=4, text=numpad[i], bg="black", fg='white'))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]['command'] = lambda x=numpad[i]: res.numberEnter(x)
        i += 1



# Calculatrice (STANDARD)
Button(calc, text='c', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray15",command=res.clear_entry).grid(row=1, column=0, pady=1)
Button(calc, text='ce', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray15",command=res.clear_all).grid(row=1, column=1, pady=1)
Button(calc, text=u'\u221A', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray15", command=res.sq_rt).grid(row=1, column=2, pady=1)
Button(calc, text='+', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray15",command=lambda: res.operation('add')).grid(row=1, column=3, pady=1)

Button(calc, text='-', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray15",command=lambda: res.operation('sub')).grid(row=2, column=3, pady=1)
Button(calc, text='*', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray15",command=lambda: res.operation('mul')).grid(row=3, column=3, pady=1)
Button(calc, text='/', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray15",command=lambda: res.operation('div')).grid(row=4, column=3, pady=1)
Button(calc, text='=', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="#00a8ff", command=res.sum_of_total).grid(row=5, column=3, pady=1)

Button(calc, text='.', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="black",command=lambda: res.numberEnter('.')).grid(row=5, column=2, pady=1)
Button(calc, text='0', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="black",command=lambda: res.numberEnter(0)).grid(row=5, column=1, pady=1)
Button(calc, text=chr(177), width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="black", command=res.PM).grid(row=5, column=0, pady=1)


# Calculatrice (SCIENTIFIQUE)

# LIGNE 6
Button(calc, text=u'\u03C0', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.pi).grid(row=6, column=0, pady=1)
Button(calc, text='e', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.e).grid(row=6,column=1,pady=1)
Button(calc, text='exp', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.exp).grid(row=6,column=2,pady=1)
Button(calc, text='mod', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20",command=lambda: res.operation('mod')).grid(row=6, column=3, pady=1)

# LIGNE 7
Button(calc, text='sin', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.sin).grid(row=7,column=0,pady=1)
Button(calc, text='cos', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.cos).grid(row=7,column=1,pady=1)
Button(calc, text='tan', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.tan).grid(row=7,column=2,pady=1)
Button(calc, text='deg', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.degrees).grid(row=7, column=3, pady=1)

# LIGNE 8
Button(calc, text='sinh', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.sinh).grid(row=8, column=0, pady=1)
Button(calc, text='cosh', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.cosh).grid(row=8, column=1, pady=1)
Button(calc, text='tanh', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.tanh).grid(row=8, column=2, pady=1)
Button(calc, text='rad', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.radians).grid(row=8, column=3, pady=1)

# LIGNE 9
Button(calc, text='log', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.log).grid(row=9,column=0,pady=1)
Button(calc, text='ln', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.ln).grid(row=9,column=1,pady=1)
Button(calc, text='log2', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.log2).grid(row=9, column=2, pady=1)
Button(calc, text='x²', width=6, height=1, font=('arial', 16, 'bold'), bd=4, fg='white', bg="gray20", command=res.carre).grid(row=9, column=3, pady=1)


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# MENU
menubar = Menu(calc)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Type de calculatrice", menu=file_menu)
file_menu.add_command(label="Calculatrice (Standard)", command=lambda: Std(root))
file_menu.add_command(label="Calculatrice (Super)", command=lambda: Sci(root))
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=lambda: Exit(root))

root.config(menu=menubar)
root.mainloop()


