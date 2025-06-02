"""Ejercicio 1: Sistema de Biblioteca

Se tiene un archivo prestamos.csv con el siguiente formato:
mes ,libro  ,apellido_nombre    ,dias_prestamo

Ejemplo:

1,El Quijote,Martinez Ana,15
1,Cien años de soledad,Garcia Luis,7
1,El Quijote,Lopez Pedro,21
2,Rayuela,Martinez Ana,14
2,Don Quijote,Gonzalez Maria,3
...
Se pide:

Recorriendo una sola vez el archivo y sin cargarlo completamente en memoria, 
realizar un corte de control indicando: cantidad de libros prestados mensualmente y dentro de cada mes, 
cantidad de préstamos y promedio de días.

Realizar una nueva lectura del archivo y armar un diccionario donde la clave será el nombre del lector 
y el dato será una lista de longitud 2: libros prestados, días totales de préstamo.

diccionario[lector] = [libros_prestados, dias_tot_prestamo]

En base al diccionario, crear un listado ordenado de mayor a menor por días totales de préstamo, 
indicando: lector - días totales. No incluir lectores con menos de 10 días totales.

ESTRUCTURA 

- LEER LINEA X LINEA

- CORTE CONTROL: OBTENER DATOS

- DICCIONARIO

- MAIN

"""

FIN_ARCHIVO = ("", "", "", "")

def leer_linea(archivo):

    linea = archivo.readline()

    if linea == "":
        resultado = FIN_ARCHIVO
    else:
        resultado = linea.rstrip().split(',') 
    
    return resultado

def procesar_datos(archivo):
    
    # salteo primera linea
    archivo.readline()

    rarchivo = leer_linea(archivo)

    while rarchivo != FIN_ARCHIVO:

        mes_actual = rarchivo[0]

        cant_dias = 0
        prestamos = 0
        promedio = 0

        print(f"\nMes actual: {mes_actual}")

        while rarchivo != FIN_ARCHIVO and rarchivo[0] == mes_actual:

            prestamos += 1
            cant_dias += int(rarchivo[3])

            rarchivo = leer_linea(archivo)

        promedio = cant_dias / prestamos

        print(f"Cantidad de prestamos: {prestamos}")
        print(f"Promedio de dias: {promedio}")
        
def obtener_diccionario(archivo):

    # salteo primera linea
    archivo.readline()
    dicc = {}
    rarchivo = leer_linea(archivo)

    while rarchivo != FIN_ARCHIVO:

        lector = rarchivo[2]

        dias_prestamo = rarchivo[3]

        dicc.setdefault(lector, [0, 0]) 

        dicc[lector][0] += 1
        dicc[lector][1] += int(dias_prestamo)

        rarchivo = leer_linea(archivo)

    return dicc 

def obtener_lista(diccionario):

    lista_ordenada = []

    for lector, datos in diccionario.items():

        dias = datos[1]

        if dias >= 10:
            lista_ordenada.append((lector, dias))
    
    lista_ordenada.sort(key=lambda x: x[1], reverse=True)

    return lista_ordenada

def mostrar_lista(lista):

    print(f"\nDatos del diccionario:")

    for lector, dias in lista:
        print(f"{lector} - {dias}")

def main():

    # primer lectura 
    archivo = open('prestamos.csv', 'r')
    procesar_datos(archivo)
    archivo.close()

    #segunda lectura
    archivo = open('prestamos.csv', 'r')
    diccionario = obtener_diccionario(archivo)
    lista = obtener_lista(diccionario)
    mostrar_lista(lista)
    archivo.close()
    
main()


