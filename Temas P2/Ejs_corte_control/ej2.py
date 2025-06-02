"""Ejercicio 2:
Se maneja un archivo inventario.csv con movimientos de stock:
semana,producto,tipo_movimiento,cantidad

Ejemplo:
4
1,Laptop Dell,entrada,20
1,Mouse Logitech,salida,15
1,Laptop Dell,salida,5
2,Teclado HP,entrada,30
2,Mouse Logitech,entrada,25
...
Se pide:

Hacer un corte de control por semana indicando: cantidad de movimientos semanales y 
dentro de cada movimiento, cantidad de entradas y salidas.

Crear un diccionario con clave=producto y valor=[stock_actual, movimientos_totales]. 
Las entradas suman, las salidas restan.

Generar un listado ordenado de menor a mayor por stock actual, mostrando: 
producto - stock actual. Excluir productos con stock negativo.

ESTRUCTURA FUNCIONES: 

- LEER LINEA ✔

- CORTE CONTROL CON DATA ✔

- GENERAR DICCIONARIO ✔

- GENERAR LISTA ✔

- MOSTRAR LISTA ✔

- MAIN ✔

"""

FIN_ARCHIVO = ("", "", "", "")

def obtener_linea(archivo):

    linea = archivo.readline()

    if linea == "":
        resultado = FIN_ARCHIVO
    else:
        resultado = linea.rstrip().split(',') #NO OLVIDAR RSTRIP().SPLIT(',')
        resultado[0] = int(resultado[0])
        resultado[3] = int(resultado[3])
    
    return resultado


def corte_control(archivo):

     # salteo primera linea
    archivo.readline()

    rarchivo = obtener_linea(archivo)

    while rarchivo != FIN_ARCHIVO:
        semana_actual = rarchivo[0]
        tot_movimientos = 0
        entradas = 0
        salidas = 0

        print(f"\nSemana Actual: {semana_actual}")

        while rarchivo != FIN_ARCHIVO and rarchivo[0] == semana_actual:

            tot_movimientos += 1

            if rarchivo[2] == 'entrada':
                entradas += rarchivo[3]
            else:
                salidas += rarchivo[3]
            
            rarchivo = obtener_linea(archivo)
        
        print(f"Movimientos totales: {tot_movimientos}")
        print(f"Entradas: {entradas}")
        print(f"Salidas: {salidas}")
        

def obtener_diccionario(archivo):

    dicc = {}
    
    # salteo primera linea
    archivo.readline()

    rarchivo = obtener_linea(archivo)

    while rarchivo != FIN_ARCHIVO:
        producto = rarchivo[1]
        cantidad = rarchivo[3]

        dicc.setdefault(producto, [0, 0])

        if rarchivo[2] == 'entrada':
            dicc[producto][0] += cantidad
            dicc[producto][1] += 1
        else:
            dicc[producto][0] -= cantidad
            dicc[producto][1] += 1
        
        rarchivo = obtener_linea(archivo)
    
    return dicc


def obtener_lista(diccionario):

    lista_ordenada = []

    for producto, movimientos in diccionario.items():

        if movimientos[0] > 0:
            lista_ordenada.append((producto, movimientos[0]))

        lista_ordenada.sort(key=lambda x: x[1], reverse=True)
    
    return lista_ordenada        

def mostrar_lista(lista):

    print(f"\nDatos del diccionario:")

    for producto, stock in lista:
        print(f"{producto} - {stock}")

def main():

    archivo = open('inventario.csv', 'r')
    corte_control(archivo)
    archivo.close()

    archivo = open('inventario.csv', 'r')
    diccionario = obtener_diccionario(archivo)
    lista = obtener_lista(diccionario)
    mostrar_lista(lista)
    archivo.close()


main()






