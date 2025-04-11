"""
--------------------------------------------------------------------------------
Escribir una funcion que reciba un texto y devuelva una lista anidada que
representa un ranking de palabras.
El texto puede tener gran cantidad de palabras, por eso se debe evitar recorrer
mas de una vez todo el texto.
La función deberá devolver una lista anidada, en la que cada sublista, este
formada por un par [palabra, cantidad de veces en el texto], ordenada por la
cantidad de veces que aparece la palabra.
Las palabras solo deben aparecer una vez en la lista.
--------------------------------------------------------------------------------
"""

def contar_palabras(texto):

    palabras_y_cantidades = []

    texto.lower()
    text_modif = list(set(texto.split())) # hace un set de palabras del texto sin repetir
    text_modif.sort()
    
    for palabra in text_modif:
        cant = texto.count(palabra)
        palabras_y_cantidades.append([palabra, cant])
    
    print(palabras_y_cantidades)



contar_palabras("arbol becerro arbol arbol mecha becerro cebra")