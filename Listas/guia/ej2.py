"""2. Escribir un programa que genere una tupla de 100 valores aleatorios. Cada uno de los
valores, debe ser entero, y estar entre 0 y 10000, inclusive; y sólo debe aparecer una
vez. Luego, se deben listar por pantalla los números que sean primos e informar
cuántos son, y la suma acumulada de los mismos."""

import random 

def es_primo(num):
    es_primo = True

    for n in range(2, num):
        if num % n == 0:
            es_primo = False
    
    if num < 2: 
        es_primo = False
    
    return es_primo

def main():

    MINIMO = 0
    MAXIMO = 10000
    CANTIDAD = 100

    numeros = random.sample(range(MINIMO, MAXIMO + 1), CANTIDAD) # genera numeros unicos!!!
    tupla_numeros = tuple(numeros)

    print(tupla_numeros)

    cant_primos = 0
    suma_acumulada = 0

    for numero in tupla_numeros:
        primo = es_primo(numero)

        if primo:
            cant_primos += 1
            suma_acumulada += numero
            print(numero)

    print(f"Hay {cant_primos} primos y su suma acumulada es de: {suma_acumulada}")

main()
