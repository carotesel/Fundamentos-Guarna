"""Ejercicio 4 (DIFÍCIL)
Descripción: Dado un archivo ordenado por día y producto, informar para cada día: el producto más vendido, el total de ventas del día, y el porcentaje de ventas del producto estrella.
Archivo: ventas_productos.txt
Contenido del archivo:
Comentario: Corte de control doble, calculo adicional del porcentaje.

PROHIBIDO USAR DICCIONARIOS
"""

FIN_ARCHIVO = ("","", "") # "" por tantos campos haya

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

#informar para cada día: el producto más vendido, el total de ventas del día, y el porcentaje de ventas del producto estrella.

def corte_control(archivo):

    linea = leer_linea_txt(archivo)

    while linea != FIN_ARCHIVO:
        dia_actual = linea[0]
        total_dia = 0
        productos_dia = {}

        while linea != FIN_ARCHIVO and linea[0] == dia_actual:
            dia, producto, cantidad = linea

            if producto not in productos_dia:
                productos_dia[producto] = 0
            productos_dia[producto] += int(cantidad)

            total_dia += int(cantidad)

            linea = leer_linea_txt(archivo)
    
    # Identificar el producto estrella
        producto_estrella = max(productos_dia, key=productos_dia.get)
        cantidad_estrella = productos_dia[producto_estrella]
        porcentaje = (cantidad_estrella / total_dia) * 100

        print(f"Día {dia_actual}:")
        print(f"  Producto más vendido: {producto_estrella} ({cantidad_estrella})")
        print(f"  Total de ventas: {total_dia}")
        print(f"  Porcentaje del producto estrella: {porcentaje:.2f}%\n")



def main():
    
    archivo = abrir_archivo("ventas_productos.txt")

    corte_control(archivo)

    archivo.close()

main()


