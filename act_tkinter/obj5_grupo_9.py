#Padron: 114021 
#Carolina Teselman
from tkinter import *
from tkinter import messagebox

def obj_5():
    raiz = Tk()

    raiz.title("Login Grupo 9")
    raiz.geometry('300x150')
    raiz.resizable(0,0)
    raiz.iconbitmap("icon.ico") 
    raiz.config(bg="red")

    usuario = StringVar()
    clave = StringVar()
    usuarios = obtener_usuarios_claves()

    myFrame = Frame(raiz)
    myFrame.pack()

    LabelUsuario = Label(myFrame, text="Usuario:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
    cuadroUsuario = Entry(myFrame, textvariable=usuario).grid(row=0,column=1, padx=10, pady=10)

    LabelClave = Label(myFrame, text="Clave:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    cuadroClave = Entry(myFrame, textvariable=clave)
    cuadroClave.config(show="*")
    cuadroClave.grid(row=1,column=1, padx=10, pady=10)

    botonEnvio = Button(myFrame, text="Enviar", command=lambda: validar(usuario.get(), clave.get(), usuarios))
    botonEnvio.grid(row=3, column=1)

    botonRegistro = Button(myFrame, text="Registrar usuario", command=lambda:abrir_ventana_registro(usuarios))
    botonRegistro.grid(row=4, column=1)

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

def validar(nombre, clave, usuarios):
    
    if nombre in usuarios:
        if clave == usuarios[nombre]:
             messagebox.showinfo("Éxito", "Usuario y clave correctos.")
        else:
            messagebox.showerror("Error", "Clave incorrecta.")

    else:
        messagebox.showerror("Error", "Usuario incorrecto.")

def abrir_ventana_registro(usuarios):
    ventana_registro = Toplevel()
    ventana_registro.title("Registro de usuario")
    ventana_registro.geometry("300x200")
    ventana_registro.config(bg="lightblue")

    usuario = StringVar()
    clave = StringVar()

    LabelUsuario = Label(ventana_registro, text="Usuario:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
    cuadroUsuario = Entry(ventana_registro, textvariable=usuario).grid(row=0,column=1, padx=10, pady=10)

    LabelClave = Label(ventana_registro, text="Clave:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    cuadroClave = Entry(ventana_registro, textvariable=clave)
    cuadroClave.config(show="*")
    cuadroClave.grid(row=1,column=1, padx=10, pady=10)

    botonEnvio = Button(ventana_registro, text="Enviar", command=lambda: registrar(usuario.get(), clave.get(), usuarios))
    botonEnvio.grid(row=3, column=1)

def registrar(nombre, clave, usuarios):

    if not nombre or not clave:
        messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
        return

    if nombre in usuarios:
        messagebox.showerror("Error", "El usuario ya existe.")
    else:
        usuarios[nombre] = clave
        messagebox.showinfo("Éxito", f"Usuario '{nombre}' registrado con éxito.")

obj_5()