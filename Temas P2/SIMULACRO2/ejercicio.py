FIN_ARCHIVO = [0, "", "", "", ""]

def leer_linea(archivo):

    linea = archivo.readline()

    if linea == "":
        resultado = FIN_ARCHIVO
    else:
        resultado = linea.rstrip().split(',')
    return resultado

def corte_control(archivo):
    rarchivo = leer_linea(archivo)

    while rarchivo != FIN_ARCHIVO:

        semana_actual = rarchivo[0]
        transacciones_semanales = 0
        libros_prestados_semanales = 0

        while rarchivo != FIN_ARCHIVO and rarchivo[0] == semana_actual:
            libros_prestados = rarchivo[2].split('-')
            transacciones_semanales += 1

            for libro in libros_prestados:
                libros_prestados_semanales += int(libro)
            
            rarchivo = leer_linea(archivo)

        
        print("SEMANA - TRANSACCIONES - LIBROS PRESTADOS")
        print(f"{semana_actual} - {transacciones_semanales} - {libros_prestados_semanales}")


def armar_diccionario(archivo):

    dicc = {}
    rarchivo = leer_linea(archivo)

    while rarchivo != FIN_ARCHIVO:

        libros_prestados = 0
        libros_devueltos = 0
        lector = rarchivo[1]

        vec_libros_prestados = rarchivo[2].split('-')
        vec_libros_devueltos = rarchivo[4].split('-')

        for i in range(3):
            libros_prestados += int(vec_libros_prestados[i])
            
        for i in range(3):
            libros_devueltos += int(vec_libros_devueltos[i])
            
        pendientes = libros_prestados - libros_devueltos

        if pendientes > 0:
            dicc.setdefault(lector, 0)
            dicc[lector] += pendientes
        
        rarchivo = leer_linea(archivo)
        
    return dicc

def listar_y_escribir(diccionario, archivo):

    lista = []

    for item, dato in diccionario.items():
        lista.append((item, dato))

    lista.sort(key=lambda x: x[1], reverse=True)

    for item in lista:
        linea = str(item[0]) + "," + str(item[1]) +"\n"
        archivo.write(linea)


    

def main():

    # ej 1
    archivo = open('prestamos.csv', 'r')
    corte_control(archivo)
    archivo.close()

    # ej 2
    archivo = open('prestamos.csv', 'r')
    dicc = armar_diccionario(archivo)
    archivo.close()

    # ej 3
    ranking = open('lectores_activos.txt', 'w')
    listar_y_escribir(dicc, ranking)
    ranking.close()



main()