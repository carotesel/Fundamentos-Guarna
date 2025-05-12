"""12. Un mol de una sustancia es igual a 6,022 . 10²³ unidades (moléculas) de esa
sustancia, el valor resultante se conoce como Número de Avogadro.
Escribir una función que dado el valor en moles del agua, retorne la cantidad de
moléculas que la componen."""

NRO_AVOGADRO = 6.022 * 10 ** 23

def moles_a_moleculas(moles):
    return moles * NRO_AVOGADRO

print(moles_a_moleculas(2))