"""2) Escribir una función que reciba una cadena de caracteres a validar, y un segundo parámetro, que
contenga una cadena con los caracteres válidos. La función debe devolver True, si la cadena a validar, está
formada sólo por caracteres válidos; en caso contrario, deberá devolver False."""

def validarCadena(cadena, parametros_validos):

    if cadena == "":
        valida = False
    else: 
        for caracter in cadena:
            if caracter.lower() not in parametros_validos.lower():
                valida = False
            else: 
                valida = True
    return valida

print(validarCadena("juan", "carolex"))