"""Ejercicio 1 (FÁCIL)
Descripción: Dado un archivo ordenado por día, informar la cantidad de ventas realizadas por día.
Archivo: ventas.txt
Contenido del archivo:
Comentario: Corte de control simple sin ciclos interiores"""

# cuando cambia el dia se hace un corte

FIN_DE_ARCHIVO = ("","","") # tiene tantas columnas como el archivo a leer y la funcion

def abrir_archivo(ruta, modo='r'):
    '''
    Abre el archivo especificado en modo lectura (por defecto),
    o lo crea si no existe. Devuelve el archivo abierto.
    '''
    try:
        archivo = open(ruta, modo)
    except FileNotFoundError:
        archivo = open(ruta, 'x') # si no lo encuentra lo crea
        archivo.close()
        archivo = open(ruta, modo)
    return archivo

def leer_linea_txt(archivo, fin_archivo=FIN_DE_ARCHIVO):
    '''
    Lee una línea de un archivo de texto y devuelve una tupla con los campos.
    Si no hay más líneas, devuelve fin_archivo.
    '''
    linea = archivo.readline()
    if linea == "":
        resultado = fin_archivo
    
    else:
        resultado = linea.rstrip().split(',')
    return resultado

def contar_ventas_por_dia(archivo):
    '''
    Realiza un corte de control por día. Cuenta cuántas ventas hubo
    por cada día en el archivo ventas.txt e imprime el resultado por pantalla.
    '''
    linea = leer_linea_txt(archivo)

    while linea != FIN_DE_ARCHIVO:
        dia_actual = linea[0]
        contador = 0

        while linea != FIN_DE_ARCHIVO and linea[0] == dia_actual:
            contador += 1
            linea = leer_linea_txt(archivo)

        print(f"Día: {dia_actual} - Ventas: {contador}")


def main():
    archivo_entrada = abrir_archivo("ventas.txt")
    contar_ventas_por_dia(archivo_entrada)
    archivo_entrada.close()

main()



