"""11. Necesitamos elegir al azar una persona, dentro de un grupo de personas. Por ello
escribiremos un programa que nos permita realizar esta operación.
El programa deberá solicitar el ingreso de los nombres y apellidos de cada uno de los
integrantes de este grupo. El ingreso de nombres finalizará cuando el usuario en lugar
de ingresar un nombre y apellido, simplemente, de enter.
A medida que se ingresan los nombres y apellidos, se debe controlar que el que se
está ingresando, no haya sido ingresado.
Una vez finalizada la carga, el programa deberá informar cual es el elegido. """

# while ingreso != ""
# if ingreso != ""
# nombre = input 
# apellido = input

import random

nombre = "a"
apellido = "a"

lista_nombres = []

while nombre != "" or apellido != "":

    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")

    if (nombre != "" and apellido != "") and [nombre, apellido] not in lista_nombres:
        lista_nombres.append([nombre, apellido])
    elif [nombre, apellido] in lista_nombres:
        print("Persona ya ingresada. Ingrese otra diferente.")

print(lista_nombres)
    
# Elegir uno al azar
if lista_nombres:
    elegido = random.choice(lista_nombres)
    print("El elegido es:", elegido[0], elegido[1])
else:
    print("No se ingresaron nombres.")
