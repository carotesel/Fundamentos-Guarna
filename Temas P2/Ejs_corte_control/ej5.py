"""Ejercicio 5:
Se registran viajes en viajes.csv:

dia,linea,chofer,pasajeros
Ejemplo:

1,Línea A,Morales Carlos,45
1,Línea B,Ruiz Ana,32
1,Línea A,Fernandez Luis,38
2,Línea C,Morales Carlos,42
2,Línea B,Diaz Maria,29
...
Se pide:

Corte de control por día mostrando: viajes totales diarios 
y dentro de cada día, cantidad de pasajeros y promedio de pasajeros.

Diccionario con clave=chofer y valor=[viajes_realizados, total_pasajeros_transportados].

Ranking de choferes ordenado de mayor a menor por total de pasajeros, 
formato: chofer - total pasajeros. Excluir choferes con menos de 100 pasajeros totales.

ESTRUCTURA 
- LEER LINEA ✔
- CORTE CONTROL ✔
- DICCIONARIO
- GENERAR LISTA
- MOSTRAR LISTA
- MAIN ✔

"""
FIN_ARCHIVO = ("", "", "", "")

def leer_linea(archivo):
    linea = archivo.readline()

    if linea == "":
        resultado = FIN_ARCHIVO
    else:
        resultado = linea.rstrip().split(',')
    return resultado

def corte_control(archivo):

    archivo.readline()
    rarchivo = leer_linea(archivo)

    while rarchivo != FIN_ARCHIVO:

        dia_actual = rarchivo[0]
        viajes_totales_diarios = 0
        cant_pasajeros = 0

        print(f"Dia actual: {dia_actual}")

        while rarchivo != FIN_ARCHIVO and rarchivo[0] == dia_actual:
            viajes_totales_diarios += 1
            cant_pasajeros += int(rarchivo[3])
            rarchivo = leer_linea(archivo)
        
        promedio = cant_pasajeros / viajes_totales_diarios

        print(f"Cantidad de viajes: {viajes_totales_diarios}")
        print(f"Promedio de pasajeros: {promedio}")



def main():

    archivo = open('viajes.csv', 'r')
    corte_control(archivo)
    archivo.close()

    archivo = open('viajes.csv', 'r')
    # diccionario
    archivo.close()

main()