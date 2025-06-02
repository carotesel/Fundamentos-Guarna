"""Ejercicio 3:
Un comercio registra sus ventas en ventas.csv:


dia,vendedor,producto,importe
Ejemplo:
1,Rodriguez Carlos,Notebook,45000
1,Gomez Ana,Mouse,1200
1,Rodriguez Carlos,Teclado,3500
2,Lopez Maria,Monitor,25000
2,Gomez Ana,Notebook,47000
...

Se pide:

Corte de control por día mostrando: total de ventas diarias y dentro de cada día, 
cantidad de transacciones e importe promedio.

Diccionario con clave=vendedor y valor=[ventas_realizadas, importe_total].

Ranking de vendedores ordenado de mayor a menor por importe total, 
formato: vendedor - importe total. 
Solo mostrar vendedores con más de $50000 en ventas.

ESTRUCTURA
- LEER LINEAS ✔

- CORTE CONTROL ✔

- GENERAR DICCIONARIO ✔

- GENERAR LISTA ORDENADA 

- MOSTRAR LISTA

- MAIN ✔

"""

FIN_ARCHIVO = ("", "", "", "")

def leer_lineas(archivo):

    linea = archivo.readline()

    if linea == "":
        resultado = FIN_ARCHIVO
    else:
        resultado = linea.rstrip().rsplit(',')
    return resultado

def corte_control(archivo):

    archivo.readline() #saltea linea

    rarchivo = leer_lineas(archivo)

    while rarchivo != FIN_ARCHIVO:

        dia_actual = rarchivo[0]

        print(f"\nDia Actual: {dia_actual}")

        tot_ventas = 0 #$
        tot_transacciones = 0 #cant transacciones

        while rarchivo[0] == dia_actual and rarchivo != FIN_ARCHIVO:

            tot_transacciones += 1
            tot_ventas += int(rarchivo[3])
            rarchivo = leer_lineas(archivo)
        
        print(f"Total transacciones: {tot_transacciones}")
        print(f"Total ventas: {tot_ventas}")

        if tot_transacciones > 0:
            promedio = tot_ventas / tot_transacciones
            print(f"Importe promedio: {promedio}")


def generar_diccionario(archivo):

    dicc = {}
    archivo.readline() #saltea linea

    rarchivo = leer_lineas(archivo)

    while rarchivo != FIN_ARCHIVO:
        vendedor = rarchivo[1]
        dicc.setdefault(vendedor, [0, 0])
        dicc[vendedor][0] += 1
        dicc[vendedor][1] += int(rarchivo[3])
        rarchivo = leer_lineas(archivo)

    return dicc

def ordenar_diccionario(diccionario):

    lista_ordenada = []

    for vendedor, datos in diccionario.items():
        if datos[1] > 50000:
            lista_ordenada.append((vendedor, datos[1]))
    
    lista_ordenada.sort(key=lambda x: x[1], reverse=True)
    return lista_ordenada

def mostrar_datos(datos_ordenados):
    print(f"\nDatos obtenidos con el diccionario:")
    for vendedor, importe in datos_ordenados:
        print(f"{vendedor}-{importe}")


def main():
    archivo = open('ventas.csv', 'r')
    corte_control(archivo)
    archivo.close()

    archivo = open('ventas.csv', 'r')
    diccionario = generar_diccionario(archivo)
    lista = ordenar_diccionario(diccionario)
    mostrar_datos(lista)
    archivo.close()

    
main()