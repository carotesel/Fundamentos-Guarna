"""5. Escribir una función que indique si los 5 dados que han sido arrojados por un jugador,
forman escalera. La función recibirá por parámetro, una tupla, con los 5 valores
obtenidos al arrojar los dados. Deberá devolver True, si forman escalera, de lo
contrario, deberá devolver, False.
Para que se de escalera, hay 3 alternativas: (1,2,3,4,5); (2,3,4,5,6) ó (3,4,5,6,1),
claro que el orden en el que aparecen los valores, no importa."""

# COMO NO PUEDE HABER VALORES REPETIDOS NO COMPARO VALOR A VALOR SINO POR TUPLA VALIDA

def es_escalera(dados):
    """Indica si los dados forman una escalera válida."""
    dados_unicos = set(dados) # con set no importa el orden y no admite numeros repetidos
    print(dados_unicos)

    # sets de combinaciones posibles
    escalera_1 = {1, 2, 3, 4, 5}
    escalera_2 = {2, 3, 4, 5, 6}
    escalera_3 = {1, 3, 4, 5, 6}

    if dados_unicos == escalera_1:
        resultado = True
    elif dados_unicos == escalera_2:
        resultado = True
    elif dados_unicos == escalera_3:
        resultado = True
    else:
        resultado = False

    return resultado

print(es_escalera((1, 2, 3, 4, 5)))  # True
print(es_escalera((5, 4, 3, 2, 1)))  # True
print(es_escalera((2, 3, 4, 5, 6)))  # True
print(es_escalera((6, 5, 4, 3, 2)))  # True
print(es_escalera((1, 3, 4, 5, 6)))  # True
print(es_escalera((6, 5, 4, 3, 1)))  # True
print(es_escalera((1, 1, 2, 3, 4)))  # False
print(es_escalera((4, 5, 6, 1, 2)))  # False
print(es_escalera((6, 1, 2, 3, 5)))  # False

