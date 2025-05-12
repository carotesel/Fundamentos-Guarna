"""5) Escribir un programa que solicite el ingreso de palabras ó frases, y a medida que se ingresan informar si se
trata de un palíndromo.
Validar que la palabra ó frase ingresada, sólo este formada por caracteres alfabéticos y por espacios en
blanco.
El ingreso de las palabras ó frases, terminará cuando el usuario de enter, sin ingresar nada.
La solución debe ser estructurada en funciones, que sigan los lineamientos de la programación
estructurada. Reutilice el código de ejercicios anteriores."""

text = "a"
CARACTERES_PERMITIDOS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,;:()áéíóúÁÉÍÓÚñÑ"

def es_palindromo(cadena):
    cadena_sin_espacios = cadena.replace(" ", "")
    if str(cadena_sin_espacios).lower() == str(cadena_sin_espacios[::-1]).lower():
        palindromo = True
    else: 
        palindromo = False
    return palindromo


def validarCadena(cadena):
    for char in cadena:
            if char.lower() not in CARACTERES_PERMITIDOS.lower():
               valida = False
            else: 
                valida = True
            return valida
    
while text != "":
    text = input("Ingrese su cadena: ")
    if text != "":
        if validarCadena(text):
                palindromo = es_palindromo(text)

                if palindromo: 
                     print("la cadena es un palindromo")
                else: 
                     print("la cadena no es un palindromo")
        else: print("cadena invalida")


