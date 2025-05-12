"""1. Escribir una función que reciba por parámetro un diccionario con el siguiente formato:
{ id_producto: [ stock_minimo, stock_actual ],..........}, donde el id_producto será la
clave, de tipo cadena; y la lista asociada a cada clave id_producto, contendrá una
dupla de valores, siendo el primero, el stock mínimo a mantener de dicho producto; y
el segundo, el stock actual del producto; ambos de tipo entero positivo.
La función debe imprimir un listado con los productos a reponer (cuyo stock_actual
sea menor al stock_minimo), indicando el id_producto y la cantidad a reponer."""

def imprimir_productos_a_reponer(productos):

    productos_reponer = []

    for id, valores in productos.items():

        if valores[1] < valores[0]:
            productos_reponer.append([id, valores[0] - valores[1]])
    return productos_reponer
    

productos = {
    "pan": [10, 8],
    "leche": [20, 25],
    "queso": [5, 2]
}

lista = imprimir_productos_a_reponer(productos)
print(lista)










