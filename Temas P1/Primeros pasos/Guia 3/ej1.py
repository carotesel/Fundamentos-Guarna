"""1. Escribir un programa que solicite el ingreso de un número y luego
calcule e informe el factorial del número ingresado."""

def calcularFactorial (n:int):
    fact = 1
    for i in range(2, n+1): #range es exclusivo al final, por eso n+1
        fact = fact * i # de 2 a 2 o de 2 a 1 ni entra al for lol
    return fact

def main():

    num = int(input("Ingrese un numero: "))
    print(f"El factorial de {num} es: {calcularFactorial(num)}")

main()


