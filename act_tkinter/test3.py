from tkinter import *

raiz = Tk()

myFrame = Frame(raiz, width=1200, height=600)
myFrame.pack()

cuadroNombre = Entry(myFrame)
cuadroNombre.grid(row=0,column=1, padx=10, pady=10)

cuadroApellido = Entry(myFrame)
cuadroApellido.grid(row=1,column=1, padx=10, pady=10)

cuadroPass = Entry(myFrame)
cuadroPass.config(show="*")
cuadroPass.grid(row=2,column=1, padx=10, pady=10)

cuadroDireccion = Entry(myFrame)
cuadroDireccion.grid(row=3,column=1, padx=10, pady=10)


nombreLabel = Label(myFrame, text="Nombre:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
ApellidoLabel = Label(myFrame, text="Apellido:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
PassLabel = Label(myFrame, text="Password:").grid(row=2, column=0, sticky="w", padx=10, pady=10)
DireccionLabel = Label(myFrame, text="Direccion:").grid(row=3, column=0, sticky="w", padx=10, pady=10)


raiz.mainloop()