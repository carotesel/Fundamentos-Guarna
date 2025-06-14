"""
ESTRUCTURA 
- LEER LINEA
- MERGE
- ESCRIBIR 
- MAIN
"""

#rstrip saca el fin de linea

DIA_MAX = 32
FIN_ARCHIVO = [DIA_MAX, 0, 0]
#FIN_ARCHIVO_MERGE = [DIA_MAX, 0, 0, 0]


def leer_linea(archivo):
    linea = archivo.readline()

    if linea == "":
        resultado = FIN_ARCHIVO
    else:
        resultado = linea.rstrip().split(',')
    return resultado


def escribir(registro, archivo):

    linea = registro[0] + ',' + registro[1] + ',' + registro[2] + ',' + registro[3] + '\n'
    #linea = ",".join(registro) + "\n"
    archivo.write(linea)

def merge(ventas1, ventas2, resultado):

    rventas1 = leer_linea(ventas1)
    rventas2 = leer_linea(ventas2)

    # si no tengo el dia max lo hago not == fin archivo
    while int(rventas1[0]) < DIA_MAX or int(rventas2[0]) < DIA_MAX:

        dia_minimo = min(int(rventas1[0]), int(rventas2[0]))

        while int(rventas1[0]) == dia_minimo:
            rventas1_modificada = rventas1 + ['SUC_1']
            escribir(rventas1_modificada, resultado)
            rventas1 = leer_linea(ventas1)
        
        while int(rventas2[0]) == dia_minimo:
            rventas2_modificada = rventas2 + ['SUC_2']
            escribir(rventas2_modificada, resultado)
            rventas2 = leer_linea(ventas2)


def punto1():

    ventas1 = open('ventas1.csv', 'r')
    ventas2 = open('ventas2.csv', 'r')
    resultado = open('ventas_resultantes.csv', 'w')

    merge(ventas1, ventas2, resultado)

    print("merge realizado correctamente")

    ventas1.close()
    ventas2.close()
    resultado.close()

# ej 2
def punto2():

    dicc = {}

    resultado = open('ventas_resultantes.csv', 'r')

    rresultado = leer_linea(resultado)

    while int(rresultado[0]) < DIA_MAX:

        dia, cod_producto, cant_vendida, sucursal = rresultado

        cod_producto = int(cod_producto)

        dicc.setdefault(cod_producto, 0)

        dicc[cod_producto] += int(cant_vendida)

        rresultado = leer_linea(resultado)

    resultado.close()
    
    return dicc


def punto3(diccionario, reposicion):

    listado = []

    for item, datos in reposicion.items():

        unidades_a_reponer = 0

        if item in diccionario:  # solo si el producto fue vendido
            unidades_a_reponer = diccionario[item] - datos[1]

        if unidades_a_reponer > 0:
            listado.append((datos[0], unidades_a_reponer))
        
    listado.sort(key=lambda x: x[1], reverse=True)

    for item in listado:

        print(f"{item[0]}, {item[1]}")



def main():

    punto1()

    reposicion = {
    45: ["Tornillo 3cm", 10],
    176: ["Clavo 5cm", 15],
    202: ["Destornillador estrella", 5],
    310: ["Martillo carpintero", 8],
    88: ["Taladro eléctrico", 2],
    }

    diccionario = punto2()
    punto3(diccionario, reposicion)

main()

        


