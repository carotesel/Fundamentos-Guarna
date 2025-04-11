"""
-----------------------------------------------------------------------------
Escribir una función que reciba una palabra, y devuelva True, si la palabra
tiene diptongo, y False, en caso contrario.
Asumir que la palabra recibida, solo esta formada por letras.
En español dos vocales en contacto se articulan como diptongo cuando:
 1) una es cerrada (i u) átona (no acentuada) y la otra es abierta (a e o)
 y viceversa.
 2) ambas son cerradas, excepto si son iguales (como en chiita), donde
 forman un hiato.
-----------------------------------------------------------------------------
"""

def hay_diptongo (palabra):

    abiertas = ["a", "e", "o", "á", "é", "ó"]
    cerradas = ["i", "u"]

    diptongos = []
    hay_diptongo = False

    for letra1 in cerradas:
        for letra2 in abiertas:
            diptongos.append(letra1 + letra2)
            diptongos.append(letra2 + letra1)
    
    diptongos.extend(["ui", "iu"])

    for i in range(len(palabra) - 1):
        par = palabra[i] + palabra[i+1]

        if par in diptongos:
            hay_diptongo = True
    
    return hay_diptongo

print(hay_diptongo("chiita"))



