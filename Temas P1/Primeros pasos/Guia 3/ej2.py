"""Escribir un programa que solicite el ingreso de valores numéricos.
El ingreso finalizará cuando el usuario haya ingresado como último
valor, un cero.
Informar el total de los valores acumulados y cuantos valores fueron
ingresados."""

def main():

    num = 1
    totalAcumulado = 0
    cantValores = 0

    while (num != 0):
        num = int(input("Ingrese un numero: "))
        
        if num != 0:
            totalAcumulado += num
            cantValores += 1

    print(f"El total acumulado es de: {totalAcumulado}")
    print(f"Se ingresaron {cantValores} numeros")

main()


