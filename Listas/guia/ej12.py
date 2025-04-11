"""12. Escribir un programa que solicite el ingreso de un texto formado sólo por sustantivos
en singular, separados uno del otro, por un blanco.
El usuario ingresará por ejemplo: “casa canción río bebé pez paraguas tórax”
El programa deberá mostrar cada una de las palabras ingresadas, seguida por su
palabra en plural, un par por línea (singular - plural), en orden alfabético.
Validar que las palabras ingresadas por el usuario, sólo contengan letras; caso
contrario, enviar un mensaje acorde y volver a solicitar el ingreso.

Las reglas a cumplir para pasar un sustantivo en singular a su plural son:

a. Agregar una “s” al final, si la palabra termina en vocal sin acento.

b. Agregar una “s” al final, si la palabra termina con una é (acentuada).

c. Si la palabra termina en “z”, la reemplazamos por “ces”.

d. Agregamos “es” al final, si la palabra termina en una consonante (a excepción de la
“s”, la “z”, y la “x”), ó si la palabra termina con las vocales acentuadas: á, í, ó, ú.

e. Si el sustantivo termina en “s” ó “x”, consideramos que el plural es igual al
singular, por lo tanto la función deberá devolver lo mismo que recibió."""

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
        plural = palabra + "s"

    elif ultima == "z":
        # Caso c: reemplazamos "z" por "ces"
        plural = palabra[:-1] + "ces"

    elif ultima in "bcdfghjklmnñprtuvwyáíóú":
        # Caso d: consonantes (excepto s, z, x) o vocales acentuadas (excepto é)
        plural = palabra + "es"

    return plural

letras = False
final = ""

while not letras:
    text = input("Ingrese un texto formado sólo por sustantivos en singular: ")
    palabras = text.split()

    todo_letras = True  # Asumo que todo está bien al principio

    for palabra in palabras:
        if not palabra.isalpha():
            todo_letras = False  # Marco que hay un error

    if todo_letras:
        letras = True  # Solo si no hubo errores
    else:
        print("Las palabras ingresadas solo pueden contener letras.")

if letras:
    palabras.sort()

    for palabra in palabras:
        plural = retornar_plural(palabra)
        final += palabra + " - " + plural + "\n"

print(final)
    






