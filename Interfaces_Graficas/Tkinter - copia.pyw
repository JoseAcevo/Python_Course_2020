"""También denominadas (GUI), son intermediarios entre el programa y el usuario.
    Formadas por un conjunto de gráficos como ventanas, botones, menús, casillas de verificación, etc, etc

Librerías Python para crear (GUI).

.-TKinter
.-WxPython
.-PyQt
.-PyGTK
.-etc, etc...
Tkinter es un puente entre Python y la librería TCL/TK """

from tkinter import *

raiz = Tk()
raiz.title("Primera ventana con Python")

raiz.resizable(1, 1)

raiz.iconbitmap("F:/Python_programing/Curso tutorizado Python/Interfaces_Graficas/favicon.ico")

raiz.geometry('700x400')

raiz.config(bg='green')

raiz.mainloop()
