"""8. Escribir un programa que genere una lista anidada, con 50 sublistas de pares de
valores aleatorios. Los valores deben estar entre -1000 y 1000, inclusive.
Luego, agregar a cada sublista de pares, un tercer elemento, que sea el MCD de los
otros dos.
Por último, suprimir de la lista, las ternas cuyo MCD sea igual a 1.
Listar las ternas resultantes."""

# lista gigante con:
    # mini listas [valor, valor2]  v y v2 estan entre (-1000 y 1000).
    # agregar a c/ sublista de pares el MCD de v y v2
    # eliminar de la lista las minilistas cuyo MCD = 1

# listar la big lista

import random
import math

CANT_ELEMENTOS = 50
MINIMO = -1000
MAXIMO = 1000

lista = []
lista_filtrada = []

def generar_lista():
    lista = []

    for i in range(CANT_ELEMENTOS):
        n1 = random.randint(MINIMO, MAXIMO)
        n2 = random.randint(MINIMO, MAXIMO)
        mcd = math.gcd(n1, n2)
        lista.append([n1, n2, mcd])
    return lista

lista = generar_lista()


print(lista)
print(" ")

for elemento in lista:
    if elemento[2] != 1:
        lista_filtrada.append(elemento)

print(lista_filtrada)



