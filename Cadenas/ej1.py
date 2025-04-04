"""1) Escribir una función que reciba una cadena de caracteres. La función deberá evaluar si la cadena recibida
representa un número binario, y en ese caso devolver True, de lo contrario, deberá devolver False. """

text = input("Ingrese el texto: ")

def es_binario(text):

    if text == "":
        es_bin = False
    else:
        for caracter in text:
            if caracter == "0" or caracter == "1":
                es_bin = True
            else: 
                es_bin = False
    return es_bin

print(es_binario(text))