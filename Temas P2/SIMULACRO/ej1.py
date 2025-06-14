"""En una empresa se lleva un control de las entradas y salidas del personal 
durante el mes. 
Estas se registran en dos archivos CSV separados: entradas.txt y salidas.txt.
Cada línea representa el ingreso o egreso de un empleado un determinado día, y contiene la siguiente información:

día,apellido_nombre,hora,sector

Por ejemplo, los archivos pueden tener el siguiente contenido:

entradas.txt
1,Ana Lopez,08:00,Producción
1,Lucas Pérez,08:15,Administración
2,Ana Lopez,08:00,Producción
3,Lucas Pérez,08:10,Administración
5,Ana Lopez,08:05,Producción

salidas.txt
1,Ana Lopez,17:00,Producción
2,Lucas Pérez,17:10,Administración
3,Ana Lopez,17:05,Producción
4,Lucas Pérez,17:00,Administración
5,Lucas Pérez,17:05,Administración

Los archivos están ordenados por día y, dentro del mismo día, por orden de aparición. Un empleado puede tener múltiples registros en diferentes días.

Se pide realizar un programa modular en Python que:


1) Recorriendo ambos archivos entradas.txt y salidas.txt sin cargar la memoria, 
genere un archivo unificado turnos.txt.

Este archivo debe contener todas las entradas y salidas ordenadas 
por día, y cada línea debe tener el siguiente formato:

día,apellido_nombre,hora,sector,movimiento

Donde el campo tipo indica si se trata de una entrada o una salida.

Por ejemplo:
1,Ana Lopez,08:00,Producción,entrada
1,Lucas Pérez,08:15,Administración,entrada
1,Ana Lopez,17:00,Producción,salida

...
Para los casos de Ana y Lucas, que venían de entradas.txt, 
se agrego "entrada" como columna adicional, 
y para el caso del movimiento de Ana proveniente 
del segundo archivo, se agrego la columna "salida"



2) Recorriendo una sola vez el archivo obtenido en el inciso anterior, 
turnos.txt, y sin cargarlo completamente en memoria,

Realice un corte de control por día y dentro de cada día, 
por tipo de turno (entrada o salida), mostrando:

- La cantidad total de registros de entrada y salida de ese día.
- Por cada tipo, la cantidad de empleados que registraron 
el turno en cada sector 
(un turno completo es uno en el cual un empleado marco su entrada y salida. 
Puede haber casos de empleados que registren únicamente entrada o salida)

Tomando el ejemplo anterior, la salida esperada sería:

Día 1:
Entradas: 2
  - Producción: 1
  - Administración: 1
Salidas: 1
  - Producción: 1


3) Realizando una nueva lectura del archivo turnos.txt, arme un diccionario donde:

- La clave sea el nombre del empleado (apellido_nombre)
- El valor sea una lista de longitud 2 con la forma:
  [cantidad de turnos registrados, cantidad de días completos]

Nuevamente, un día completo se considera cuando un mismo empleado tiene tanto una entrada como una salida en el mismo día.

Al finalizar:

- Mostrar por consola los empleados que tienen al menos 3 días completos, ordenados de mayor a menor por cantidad de días completos.

Recomendación del print:
Apellido Nombre — Turnos registrados: X — Días completos: Y"""

DIA_MAX = 32
FIN_ARCHIVO = [DIA_MAX, "", 0, ""]
FIN_ARCHIVO_TURNOS = [DIA_MAX, "", 0, "", ""]


def leer_linea(archivo, fin_archivo):

    linea = archivo.readline()

    if linea == "":
        resultado = fin_archivo
    else:
        resultado = linea.rstrip().split(',')
        resultado[0] = int(resultado[0])
    return resultado

def escribir(registro, archivo):
    linea = str(registro[0]) + ',' + str(registro[1]) + ',' + str(registro[2]) + ',' + str(registro[3]) + ',' + str(registro[4]) + '\n'
    archivo.write(linea) 


def merge(entradas, salidas, aresultante):
    
    rentradas = leer_linea(entradas, FIN_ARCHIVO)
    rsalidas = leer_linea(salidas, FIN_ARCHIVO)

    while rentradas[0] < DIA_MAX or rsalidas[0] < DIA_MAX:
        
        dia_min = min(rentradas[0], rsalidas[0])
        
        while rentradas[0] < DIA_MAX and rentradas[0] == dia_min:
            rentradas_modificado = rentradas + ['entrada']
            escribir(rentradas_modificado, aresultante)
            rentradas = leer_linea(entradas, FIN_ARCHIVO)

        while rsalidas[0] < DIA_MAX and rsalidas[0] == dia_min:
            rsalidas_modificado = rsalidas + ['salida']
            escribir(rsalidas_modificado, aresultante)
            rsalidas = leer_linea(salidas, FIN_ARCHIVO)


def corte_control(turnos):

    rturnos = leer_linea(turnos, FIN_ARCHIVO_TURNOS)

    while rturnos != FIN_ARCHIVO_TURNOS:

        dia_actual = rturnos[0]
        entradas_admin= 0
        entradas_prod = 0
        salidas_admin = 0
        salidas_prod = 0

        while rturnos != FIN_ARCHIVO_TURNOS and rturnos[0] == dia_actual:

            if rturnos[4] == "entrada":
                if rturnos[3] == "Produccion":
                    entradas_prod += 1
                else:
                    entradas_admin += 1
            else:
                if rturnos[3] == "Produccion":
                    salidas_prod += 1
                else:
                    salidas_admin += 1
            rturnos= leer_linea(turnos, FIN_ARCHIVO_TURNOS)

        print(f"Dia: {dia_actual}")
        print(f"Entradas: {entradas_admin + entradas_prod}")
        print(f"  - Producción: {entradas_prod}")
        print(f"  - Administración: {entradas_admin}")
        print(f"Salidas: {salidas_admin + salidas_prod}")
        print(f"  - Producción: {salidas_prod}")
        print(f"  - Administración: {salidas_admin}")




def main():
    
    # ej 1 
    entradas = open('entradas.csv', 'r')
    salidas = open('salidas.csv', 'r')
    turnos = open('turnos.txt', 'w')

    merge(entradas, salidas, turnos)

    entradas.close()
    salidas.close()
    turnos.close()

    #ej 2
    turnos = open('turnos.txt', 'r')
    corte_control(turnos)
    turnos.close()



main()