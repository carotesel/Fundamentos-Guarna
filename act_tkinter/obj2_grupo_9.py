#Padron: 114021 
#Carolina Teselman
from tkinter import *

def obj_2():
    raiz = Tk()

    raiz.title("Login Grupo 9")
    raiz.geometry('300x130')
    raiz.resizable(0,0)
    raiz.iconbitmap("icon.png") 
    raiz.config(bg="red")

    usuario = StringVar()
    clave = StringVar()

    myFrame = Frame(raiz, width=300, height=130)
    myFrame.pack(padx=20, pady=20)

    LabelUsuario = Label(myFrame, text="Usuario:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
    cuadroUsuario = Entry(myFrame, textvariable=usuario).grid(row=0,column=1, padx=10, pady=10)

    LabelClave = Label(myFrame, text="Clave:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    cuadroClave = Entry(myFrame, textvariable=clave)
    cuadroClave.config(show="*")
    cuadroClave.grid(row=1,column=1, padx=10, pady=10)

    raiz.mainloop()

obj_2()


