"""6. De igual modo que el ejercicio anterior, escribir una función para cada uno de los
posibles casos:
Generala: 5 dados de igual valor
Póker: 4 dados iguales y 1 distinto
Full: 3 dados iguales y otros 2 iguales"""

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

print(definir_juego((5, 5, 5, 5, 5)))  # Generala
print(definir_juego((3, 3, 3, 3, 2)))  # Póker
print(definir_juego((6, 6, 2, 2, 6)))  # Full
print(definir_juego((1, 2, 3, 4, 5)))  # Ninguna

        




        

