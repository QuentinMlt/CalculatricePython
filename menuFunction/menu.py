import tkinter
import tkinter.messagebox


def Exit(root):
    if tkinter.messagebox.askyesno("Calculatrice Iskernel Python", "Voulez-vous quittez l'application ?") > 0:
        root.destroy()
        return


def Sci(root):
    root.resizable(width=False, height=False)
    root.geometry("378x500+0+0")


def Std(root):
    root.resizable(width=False, height=False)
    root.geometry("378x308+0+0")
