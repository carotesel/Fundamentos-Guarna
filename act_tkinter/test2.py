from tkinter import *

root = Tk()

myFrame = Frame(root, width=500, height=400)

myFrame.pack()

myImage = PhotoImage(file="michi.gif")

Label(myFrame, text="boca nasheeee", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)

Label(myFrame, image=myImage).place(x=100, y=100)

root.mainloop()