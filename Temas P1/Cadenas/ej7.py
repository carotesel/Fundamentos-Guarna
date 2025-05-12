"""7) Escribir una función que recibirá por parámetro, una palabra, que representa un sustantivo
en singular.
La función deberá devolver, el plural de dicho sustantivo, aplicando las siguientes reglas:
a. Agregar una “s” al final, si la palabra termina en vocal sin acento.
b. Agregar una “s” al final, si la palabra termina con una é (acentuada).
c. Si la palabra termina en “z”, la reemplazamos por “ces”.
d. Agregamos “es” al final, si la palabra termina en una consonante (a excepción de la “s”, la
“z”, y la “x”), ó si la palabra termina con las vocales acentuadas: á, í, ó, ú.
e. Si el sustantivo termina en “s” ó “x”, entonces el plural es igual al singular, por lo tanto la
función deberá devolver lo mismo que recibió. """

def retornar_plural(palabra):
    """Devuelve el plural de un sustantivo en singular, siguiendo las reglas del enunciado."""
    plural = palabra
    ultima = palabra[-1]

    if ultima == "s" or ultima == "x":
        # Caso e: se mantiene igual
        plural = palabra

    elif ultima in "aeiou":
        # Caso a: termina en vocal sin acento
        plural = palabra + "s"

    elif ultima == "é":
        # Caso b: reemplazamos "é" por "e" y agregamos "s"
        plural = palabra.replace("é", "e") + "s"

    elif ultima == "z":
        # Caso c: reemplazamos "z" por "ces"
        plural = palabra[:-1] + "ces"

    elif ultima in "bcdfghjklmnñprtuvwyáíóú":
        # Caso d: consonantes (excepto s, z, x) o vocales acentuadas (excepto é)
        plural = palabra + "es"

    return plural



