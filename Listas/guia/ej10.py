"""10. Si para el ejercicio anterior, usaste el método count; y eliminaste a través del método
pop ó con la función del(), los valores que aparecían más de una vez; reescribí la
función pero sin utilizar ninguna de estas alternativas. """

import random

def verificar_tupla(tupla):
    resultado = []

    for valor in set(tupla):
        #cantidad = tupla.count(valor)

        cantidad = 0

        for elemento in tupla:
            if elemento == valor:
                cantidad+= 1 

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