#Padron: 114021 
#Carolina Teselman
from tkinter import *
from tkinter import messagebox

def obj_4():
    raiz = Tk()

    raiz.title("Login Grupo 9")
    raiz.geometry('300x130')
    raiz.resizable(0,0)
    raiz.iconbitmap("icon.png") 
    raiz.config(bg="red")

    usuario = StringVar()
    clave = StringVar()

    myFrame = Frame(raiz)
    myFrame.pack()

    LabelUsuario = Label(myFrame, text="Usuario:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
    cuadroUsuario = Entry(myFrame, textvariable=usuario).grid(row=0,column=1, padx=10, pady=10)

    LabelClave = Label(myFrame, text="Clave:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    cuadroClave = Entry(myFrame, textvariable=clave)
    cuadroClave.config(show="*")
    cuadroClave.grid(row=1,column=1, padx=10, pady=10)

    botonEnvio = Button(myFrame, text="Enviar", command=lambda: validar(usuario.get(), clave.get()))
    botonEnvio.grid(row=3, column=1)


    raiz.mainloop()


def obtener_usuarios_claves():
    usuarios = {
    "carolina": "clave123",
    "damian": "abc456",
    "joaquin": "pass789",
    "fabricio": "aguantehuracan",
    "gabriel": "ilovepython",
    "faustina": "fundamentos2025"
    }

    return usuarios

def validar(nombre, clave):
    usuarios = obtener_usuarios_claves()
    
    if nombre in usuarios:
        if clave == usuarios[nombre]:
             messagebox.showinfo("Éxito", "Usuario y clave correctos.")
        else:
            messagebox.showerror("Error", "Clave incorrecta.")

    else:
        messagebox.showerror("Error", "Usuario incorrecto.")

obj_4()



    





    




