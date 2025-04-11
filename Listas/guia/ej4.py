"""4. Escribir un programa que solicite al usuario el ingreso de un número natural N, y
luego informe, primero los números primos que hay entre 0 y el número ingresado, y
luego los números que no son primos. Para la solución, debe implementar el método
de la Criba de Eratóstenes, que permite hallar los números primos menores que un
número natural dado.
En base a una lista con todos los números naturales comprendidos entre 2 y N, se descarta
primero el 2 y todos sus múltiplos. Luego se repite el proceso para el primer número que
aparece en la lista y todos sus múltiplos. Así sucesivamente hasta que el cuadrado del primer
número que aparece como primero en la lista resultante, sea mayor a N."""

def criba_eratostenes(n):
    """Devuelve dos listas: los números primos y los no primos hasta n."""
    lista_numeros = list(range(2, n + 1))
    no_primos = []

    indice = 0
    while indice < len(lista_numeros) and lista_numeros[indice] * lista_numeros[indice] <= n:
        numero = lista_numeros[indice]

        for multiplo in range(numero * 2, n + 1, numero):
            if multiplo in lista_numeros:
                no_primos.append(multiplo)
                lista_numeros.remove(multiplo)

        indice += 1

    primos = lista_numeros

    return primos, no_primos


def main():
    """Pide un número y muestra los primos y no primos."""
    n = int(input("Ingrese un número natural: "))

    primos, no_primos = criba_eratostenes(n)

    print("Números primos:")
    print(primos)
    print()
    print("Números no primos:")
    print(no_primos)

main()
