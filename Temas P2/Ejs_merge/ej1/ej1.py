"""Ejercicio 1 (FÁCIL):
Fusionar archivos de temperaturas diarias de dos estaciones meteorológicas.
Objetivo: crear un archivo único que indique de qué estación viene cada temperatura.

Cada archivo tiene: dia, temperatura

estacionA.txt:
1,23
2,25
4,21
5,22
7,24

estacionB.txt:
1,22
3,24
4,20
6,23
7,25

ESTRUCTURA:
- LEER LINEAS (DIFERENTE) ✔
- MERGE ✔
- GUARDAR ✔
- MAIN ✔
"""
# el orden de los while en merge determina el criterio de cual va primero ante un mismo dia

MAX_DIA = 10
FIN_ARCHIVO = [MAX_DIA, 0]

def leer_lineas(archivo):

    linea = archivo.readline()

    if linea == "":
        resultado = FIN_ARCHIVO
    else:
        resultado = linea.rstrip().split(',')
    return resultado

def guardar(registro, archivo):
    linea = str(registro[0]) + ',' + str(registro[1]) + ',' + registro[2]+ '\n'
    archivo.write(linea)



def merge(archivo1, archivo2, union):

    rarchivo1 = leer_lineas(archivo1)
    rarchivo2 = leer_lineas(archivo2)

    while int(rarchivo1[0]) < MAX_DIA or int(rarchivo2[0]) < MAX_DIA:
        dia_min = min(rarchivo1[0], rarchivo2[0])

        while rarchivo1[0] == dia_min:
            registro_con_estacion_1 = rarchivo1 + ['estacion_1']
            guardar(registro_con_estacion_1, union)
            rarchivo1 = leer_lineas(archivo1)
        
        while rarchivo2[0] == dia_min:
            registro_con_estacion_2 = rarchivo2 + ['estacion_2']
            guardar(registro_con_estacion_2, union)
            rarchivo2 = leer_lineas(archivo2)



def main():
    archivo_1 = open('estacionA.txt', 'r')
    archivo_2 = open('estacionB.txt', 'r')
    archivo_union = open('estaciones_totales.txt','w')

    merge(archivo_1,archivo_2,archivo_union)

    archivo_1.close()
    archivo_2.close()
    archivo_union.close()


main()

