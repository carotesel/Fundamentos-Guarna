from tkinter import *
from tkinter import messagebox

raiz = Tk()

raiz.title("Ingreso de Datos")

myFrame = Frame(raiz, width=500, height=300)
myFrame.pack(padx=20, pady=20)

mi_nombre = StringVar()
mi_apellido = StringVar()
mi_mail = StringVar()
hecho_por = StringVar(value="Hecho por: NOMBRE APELLIDO")

def validar_cadena(cadena):
    return cadena.isalpha() and len(cadena) <= 25

def validar_mail(cadena):
    cant_arrobas = cadena.count("@")
    pos_arroba = cadena.find("@")
    largo = len(cadena)
    es_valido = False

    if (cant_arrobas == 1 and largo <= 20) and (pos_arroba != 0 or pos_arroba != largo - 1):
        es_valido = True
    return es_valido



LabelNombre = Label(myFrame, text="Nombre:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
cuadroNombre = Entry(myFrame, textvariable=mi_nombre)
cuadroNombre.grid(row=0,column=1, padx=10, pady=10)

ApellidoLabel = Label(myFrame, text="Apellido:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
cuadroApellido = Entry(myFrame, textvariable=mi_apellido)
cuadroApellido.grid(row=1,column=1, padx=10, pady=10)

MailLabel = Label(myFrame, text="Mail:").grid(row=2, column=0, sticky="w", padx=10, pady=10)
cuadroMail = Entry(myFrame, textvariable=mi_mail)
cuadroMail.grid(row=2,column=1, padx=10, pady=10)

def enviar_form():
    nombre = mi_nombre.get()
    apellido = mi_apellido.get()
    mail = mi_mail.get()

    if not validar_cadena(nombre):
        messagebox.showerror("Error", "El nombre debe tener solo letras y como máximo 25 caracteres.")
    
    if not validar_cadena(apellido):
        messagebox.showerror("Error", "El apellido debe tener solo letras y como máximo 25 caracteres.")
        return

    if not validar_mail(mail):
        messagebox.showerror("Error", "El mail debe tener un solo '@', no al inicio ni al final, y máximo 20 caracteres.")
        return

    hecho_por.set(f"Hecho por: {mi_nombre.get()} {mi_apellido.get()}")

    messagebox.showinfo("Éxito", "Los datos fueron recibidos correctamente.")


    # Limpiar los campos
    mi_nombre.set("")
    mi_apellido.set("")
    mi_mail.set("")

Label(raiz, textvariable=hecho_por).pack(side="bottom", pady=10)

botonEnvio = Button(raiz, text="Enviar", command = enviar_form).pack()

raiz.mainloop()

