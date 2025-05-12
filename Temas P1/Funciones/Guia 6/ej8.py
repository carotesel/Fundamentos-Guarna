"""8. Escribir un programa que solicite al usuario el ingreso de una serie de palabras de
a una por vez. El ingreso termina cuando el usuario, en lugar de ingresar una
palabra, sólo presione la tecla Enter.
Controlar que las palabras ingresadas tengan al menos 5 caracteres y que estén
formadas solo por la combinación de las vocales y las letras consonantes
utilizadas en el sistema de numeración romano (I, V, X, L, C, D, M). Dar aviso al
usuario cuando una palabra no cumpla con esta condición, y luego solicitar el
ingreso de la siguiente."""

CARACTERES_PERMITIDOS = "ivxlcdmaeiouáéíóú"

palabra = "a"

while palabra != "":
    if palabra != "":
        prohibida = False
        palabra = input("Ingrese una palabra o enter para terminar: ")

    for caracter in palabra:
        if caracter.lower() not in CARACTERES_PERMITIDOS:
            prohibida = True
    
    if prohibida:
        print("la palabra contiene caracteres no permitidos.")



    



