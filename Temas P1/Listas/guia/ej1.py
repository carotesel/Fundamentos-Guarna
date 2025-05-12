"""1. Escribir una función que reciba por parámetro una tupla de números enteros. La
función deberá devolver 1, si la tupla se encuentra ordenada en forma creciente; -1 si
la tupla está ordenada en forma decreciente; ó 0 si la tupla está desordenada."""

tupla = (1, 2, 3, 4)
tupla2 = (4, 3, 2, 1)
tupla3 = (2, 2, 2, 2)

ORDEN_CREC = 1
ORDEN_DECR = -1
DESORDENADO = 0

def esta_ordenada(tupla):
    hay_creciente = False
    hay_decreciente = False

    for i in range(1, len(tupla)):
        if tupla[i] > tupla[i-1]:
            hay_creciente = True
        elif tupla[i] < tupla[i-1]:
            hay_decreciente = True
        
        if hay_creciente and not hay_decreciente:
            resultado = ORDEN_CREC
        elif hay_decreciente and not hay_creciente:
            resultado = ORDEN_DECR
        else:
            resultado = DESORDENADO

    return resultado


print(esta_ordenada(tupla))
print(esta_ordenada(tupla2))
print(esta_ordenada(tupla3))



    
