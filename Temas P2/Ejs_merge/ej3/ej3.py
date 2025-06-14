"""Ejercicio 3 (FÁCIL): (7)
Fusionar listados de libros de dos bibliotecas.
Cada archivo tiene: id_libro, nombre_libro
Objetivo: unir todos los libros indicando la biblioteca.

biblioA.txt:
1,1984
2,Rayuela
3,El Aleph
4,Ficciones
6,Cien años de soledad

biblioB.txt:
2,Crimen y castigo
3,Don Quijote
5,La Metamorfosis
6,El Túnel
7,Bajo la misma estrella

ESTRUCTURA
- LEER LINEAS ✔
- MERGE ✔
- ESCRIBIR ✔
- MAIN ✔
"""

MAX_ID = 10
FIN_ARCHIVO = [MAX_ID, ""]

def leer_lineas(archivo):

    linea = archivo.readline()

    if linea == "":
        resultado = FIN_ARCHIVO
    else:
        resultado = linea.rstrip().split(',')
    return resultado


def escribir(registro, archivo):
    linea = registro[0] + ',' + registro[1] + ',' + registro[2] + '\n'
    archivo.write(linea)

def merge(biblioA, biblioB, totales):

    rbiblioA = leer_lineas(biblioA)
    rbiblioB = leer_lineas(biblioB)

    while int(rbiblioA[0]) < MAX_ID or int(rbiblioB[0]) < MAX_ID:

        id_actual = min(int(rbiblioA[0]), int(rbiblioB[0]))

        while id_actual == int(rbiblioA[0]):
            registro_con_bib_A = rbiblioA + ['biblioA']
            escribir(registro_con_bib_A, totales)
            rbiblioA = leer_lineas(biblioA)

        while id_actual == int(rbiblioB[0]):
            registro_con_bib_B = rbiblioB + ['biblioB']
            escribir(registro_con_bib_B, totales)
            rbiblioB = leer_lineas(biblioB)



def main():

    biblioA = open('biblioA.txt', 'r')
    biblioB = open('biblioB.txt', 'r')
    totales = open('resultado.txt', 'w')

    merge(biblioA, biblioB, totales)

    biblioA.close()
    biblioB.close()
    totales.close()

main()



