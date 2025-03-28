"""10. Escribir una función que reciba a través de sus parámetros, dos valores enteros,
y devuelva True, si el primer parámetro es múltiplo del segundo, de lo contrario
debe devolver False. No te preocupes por el caso que uno ó ambos valores
recibidos sea igual a cero.
Dale a la función el es_multiplo_de."""

def es_multiplo_de(num1, num2):
    if num1 % num2 == 0:
        es_mult = True
    else :
        es_mult = False
    return es_mult

print(es_multiplo_de(20, 4))