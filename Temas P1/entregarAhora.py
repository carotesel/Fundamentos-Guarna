"""Escribir una función elegir en Python para decidir asociarse o no a un club. Esta función debe
devolver True si el club es aceptado, False de lo contrario.

La función recibe dos listas y un entero: una de actividades (actividades que se realizan en el club),
otra de actividades_deseadas (son las actividades que al usuario le gustaría realizar) y un valor de cuota.

El club se aceptará si:

- Si realizan por lo menos dos actividades deseadas y el valor de la cuota es menor o igual a

MAX_CUOTA = 6000

Ejemplos:

lista_1 = ['natación', 'gimnasio', 'voley', 'futbol']

lista_2 = ['natación', 'voley', 'gimnasio']

lista_3 = ['natación', 'futbol', 'karate']

elegir(lista_1, lista_2, 5000) ---> True

elegir(lista_1, lista_3, 5000) ---> True

elegir(lista_1, lista_3, 7000) ---> False

elegir(lista_2, lista_3, 100) ---> False"""

MAX_CUOTA = 6000
MIN_COINCIDENCIAS = 2

def elegir(actividades, actividades_deseadas, cuota):
    i = 0
    coincidencias = 0

    while i < len(actividades_deseadas):
        if actividades_deseadas[i] in actividades:
            coincidencias += 1
        i += 1

    return coincidencias >= MIN_COINCIDENCIAS and cuota <= MAX_CUOTA

lista_1 = ['natación', 'gimnasio', 'voley', 'futbol']
lista_2 = ['natación', 'voley', 'gimnasio']
lista_3 = ['natación', 'futbol', 'karate']

print(elegir(lista_1, lista_2, 5000))  # devuelve True
print(elegir(lista_1, lista_3, 5000))  # devuelve True
print(elegir(lista_1, lista_3, 7000))  # devuelve False
print(elegir(lista_2, lista_3, 100))   # devuelve False



