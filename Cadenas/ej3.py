"""3) Escribir una función que reciba una dirección de mail, y devuelva True ó False, en función de haber
evaluado que dicha dirección está bien formada.
Escribir una función que reciba una cadena de caracteres que representa una dirección de mail. La
función deberá devolver True ó False, en función de haber evaluado que dicha dirección está bien
formada.
Se debe controla que:
a. Que no contenga blancos
b. Que sólo se utilicen letras y/o números para la parte del nombre, delante de la @
c. Que haya exactamente una arroba
d. Que los nombres de dominio sean: fi.uba.ar ó gmail.com """

def validarMail(mail):
    es_valido = True

    if " " in mail: es_valido = False
    elif not mail[ :mail.find("@")].isalnum(): es_valido = False
    elif mail.count("@") != 1: es_valido = False
    elif mail.count("fi.uba.ar") == 0 and mail.count("gmail.com") == 0: es_valido = False
    return es_valido

print(validarMail("carot@gmail.com"))