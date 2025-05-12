"""9. Escribir una función que reciba una tupla de N números enteros.
La función deberá devolver una lista formada por pares de elementos, donde el primer
elemento, será uno de los valores que venía en la tupla, y el segundo elemento, la
cantidad de veces que dicho valor aparecía en la tupla. La lista debe estar ordenada
por el primer elemento del par.
Los valores sólo deben aparecer una única vez en la lista.
Pruebe su función, con tuplas generadas aleatoriamente:
a. Con 100 elementos, con valores entre 0 y 10.
b. Con 1000 elementos, con valores entre -10 y 10.
c. Con 5000 elementos, con valores pares entre 2 y 20."""

# recibo tupla de enteros que pueden estar repetidos 
# de cada numero hago un set pa que no se repitan y del set cuento cuantos hay en cada uno
# nueva tupla que sea (valor, cantidad)

import random

def verificar_tupla(tupla):
    resultado = []

    for valor in set(tupla):
        cantidad = tupla.count(valor)
        resultado.append([valor, cantidad])
    
    resultado.sort() # ordena x el primer elemento del par
    return resultado

lista = []

# Generar las tuplas
tupla_100 = tuple(random.randint(0, 10) for _ in range(100))
tupla_1000 = tuple(random.randint(-10, 10) for _ in range(1000))

pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
tupla_5000 = tuple(random.choice(pares) for _ in range(5000))

lista = verificar_tupla(tupla_1000)

print(lista)