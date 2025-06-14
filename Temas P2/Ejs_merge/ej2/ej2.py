"""Ejercicio 2 (FÁCIL):
Fusionar listas de precios de productos de dos proveedores.
Cada archivo tiene: producto_id, precio
Objetivo: crear un archivo con todos los precios indicando de qué proveedor vienen.

proveedorA.txt:
101,50
102,75
103,60
104,80
105,55

proveedorB.txt:
101,52
102,70
106,65
107,90
108,45

ESTRUCTURA
- LEER LINEAS ✔
- MERGE ✔
- ESCRIBIR ✔
- MAIN ✔

"""
MAX_ID = 110
FIN_ARCHIVO = [MAX_ID, ""]

def leer_lineas(archivo):

    linea = archivo.readline()

    if linea == "":
        resultado = FIN_ARCHIVO
    else:
        resultado = linea.rstrip().split(',')
    return resultado


def escribir(registro, archivo):
    linea = registro[0] + "," + registro[1] + "," +  registro[2] + "\n"
    archivo.write(linea)

def merge(provA, provB, totales):

    rprovA = leer_lineas(provA)
    rprovB = leer_lineas(provB)

    while int(rprovA[0]) < MAX_ID or int(rprovB[0]) < MAX_ID:

        id_min = min(int(rprovA[0]), int(rprovB[0]))

        while int(rprovA[0]) == id_min:
            registro_con_prov_A = rprovA + ['prov_a']
            escribir(registro_con_prov_A, totales)
            rprovA = leer_lineas(provA)
        
        while int(rprovB[0]) == id_min:
            registro_con_prov_B = rprovB + ['prov_b']
            escribir(registro_con_prov_B, totales)
            rprovB = leer_lineas(provB)



def main():

    proveedorA = open('proveedorA.txt', 'r')
    proveedorB = open('proveedorB.txt', 'r')
    proveedores_totales = open('proveedores_totales.txt', 'w')

    merge(proveedorA, proveedorB, proveedores_totales)

    proveedorA.close()
    proveedorB.close()
    proveedores_totales.close()

main()