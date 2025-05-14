from tkinter import *

raiz = Tk()

raiz.title("Pruebas")

#raiz.resizable(1, 1) # w = False y h = False

raiz.iconbitmap("icon.ico") # no anda en mac

#raiz.geometry("650x350")

raiz.config(bg="blue")

miFrame = Frame()

#miFrame.pack(side="left", anchor="n")

miFrame.pack(fill="x")

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd="30")

miFrame.config(relief="groove")

miFrame.config(cursor="pirate")

raiz.mainloop()



