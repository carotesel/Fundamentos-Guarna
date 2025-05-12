"""7. Ahora vamos a escribir un programa que simule una situación de juego, utilizando las
funciones escritas en los puntos 3 y 4; y sumando nuevas funciones para lo que se
solicite en este punto específicamente.
Escribir un programa que genere 1000 tiradas aleatorias, de los 5 dados.
Por cada tirada, se debe clasificar si corresponde a alguna de las categorías para las
que hemos escrito las funciones, ó a ninguna de ellas.
El programa deberá emitir un informe que indique la cantidad de tiradas coincidentes
con cada categoría (incluída que no coincide con ninguna categoría), y el % que
representa cada una."""

import random

CANTIDAD_TIRADAS = 1000
MINIMO = 1
MAXIMO = 6
CANTIDAD_DADOS = 5

tiradas = []
categorias = []
cantidad_por_categoria = []

# generar 1000 tiradas aleatorias de 5 dados
# clasificar categoria (generala, poker, full, ninguna)
# informar cantidad de cada categoria (poker 5, full 2 etc)
# informar % de cada categoria sobre el total

def definir_juego(dados):
    cantidades = []
    
    for dado in set(dados): # set es para no revisar el mismo nro 2 veces!!!!
        cantidad = dados.count(dado)
        cantidades.append(cantidad)

    if 5 in cantidades:
            jugada = "Generala"
    elif 4 in cantidades:
            jugada = "Póker"
    elif 3 in cantidades and 2 in cantidades:
            jugada = "Full"
    else:
            jugada = "Ninguna"
    return jugada        

def generar_tiradas():
    tiradas = []

    dados = []
    
    for i in range(CANTIDAD_TIRADAS):
        
        for j in range(CANTIDAD_DADOS):
            dado = random.randint(MINIMO, MAXIMO)
            dados.append(dado)
        
        tiradas.append(tuple(dados))  # Guardamos la tirada como una tupla

    return tiradas

def contar_categorias(categorias):
    cantidad_por_categoria = []
    categorias_sin_repetir = set(categorias)
    
    for categoria in categorias_sin_repetir:
        cantidad = categorias.count(categoria)
        cantidad_por_categoria.append((categoria, cantidad))
    
    return cantidad_por_categoria

def informar_resultados(cantidad_por_categoria):
    """Informa los resultados: cantidad y porcentaje de cada categoría."""
    print("Resultados:")
    print()
    
    for categoria, cantidad in cantidad_por_categoria:
        porcentaje = (cantidad / CANTIDAD_TIRADAS) * 100
        print(f"{categoria}: {cantidad} tiradas ({porcentaje:.2f}%)")

# Programa principal
def main():
    tiradas = generar_tiradas()
    categorias = []
    
    for tirada in tiradas:
        categoria = definir_juego(tirada)
        categorias.append(categoria)
    
    cantidad_por_categoria = contar_categorias(categorias)

    print(cantidad_por_categoria)
    
    informar_resultados(cantidad_por_categoria)

main()

