"""Ejercicio 2 (FÁCIL)
Descripción: Dado un archivo con fechas de ingreso de empleados ordenado por fecha, 
informar la cantidad de empleados ingresados por mes.
Archivo: empleados.txt
Comentario: Requiere parseo de fecha con `split('-')` para poder tomar el mes de forma individual.
"""

FIN_ARCHIVO = ("","") # "" por tantos campos haya

def abrir_archivo(ruta, modo='r'):
    try:
        archivo = open(ruta, modo)
    except FileNotFoundError:
        archivo = open(ruta, 'x')
        archivo.close
        archivo = open(ruta, modo)
    return archivo
    
def leer_linea_txt(archivo, fin_archivo=FIN_ARCHIVO):
    linea = archivo.readline()

    if linea == "":
        resultado = fin_archivo
    else:
        resultado = linea.rstrip().split(',')
    return resultado

def contar_empleados_mes(archivo):

    linea = leer_linea_txt(archivo)
    dia, mes, anio = linea[0].split('-')

    while linea != FIN_ARCHIVO:
        mes_actual = mes
        contador = 0

        while linea!= FIN_ARCHIVO and mes == mes_actual:
            contador += 1

            linea = leer_linea_txt(archivo)

            if linea != FIN_ARCHIVO:
                anio, mes, dia = linea[0].split('-')
            
        print(f"Mes {mes_actual}: {contador}")

def main():
    
    archivo = abrir_archivo("empleados.txt")

    contar_empleados_mes(archivo)

    archivo.close()

main()




