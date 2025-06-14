"""ESTRUCTURA
- LEER LINEA
- MERGE 
- MAIN"""

MAX_DIA = 6
FIN_ARCHIVO = [MAX_DIA, "", 0, "", 0]

def leer_linea(archivo):
    linea = archivo.readline()

    if linea == "":
        resultado = FIN_ARCHIVO
    else:
        resultado = linea.rstrip().split(',')
    return resultado

def merge(america, europa, mix):

    ramerica = leer_linea(america)
    reuropa = leer_linea(europa)

    while ramerica != FIN_ARCHIVO or reuropa != FIN_ARCHIVO:

        dia_min = min(ramerica[0], reuropa[0])

        while reuropa != FIN_ARCHIVO and reuropa[0] == dia_min:
            reuropa_modif = reuropa + ['EUROCOPA']
            linea = f"{reuropa_modif[0]},{reuropa_modif[1]},{reuropa_modif[2]},{reuropa_modif[3]},{reuropa_modif[4]},{reuropa_modif[5]}\n"
            mix.write(linea)
            reuropa = leer_linea(europa)
        

        while ramerica != FIN_ARCHIVO and ramerica[0] == dia_min:
            ram_modif = ramerica + ['COPA AMERICA']
            linea = f"{ram_modif[0]},{ram_modif[1]},{ram_modif[2]},{ram_modif[3]},{ram_modif[4]},{ram_modif[5]}\n"
            mix.write(linea)
            ramerica = leer_linea(america)


def generar_dicc(mix):

    dicc = {}
    rmix = leer_linea(mix)

    while rmix != FIN_ARCHIVO:

        pais1 = rmix[1]
        res1 = int(rmix[2])
        pais2 = rmix[3]
        res2 = int(rmix[4])

        dicc.setdefault(pais1, [0, 0, 0])
        dicc.setdefault(pais2, [0, 0, 0])

        if res1 > res2:
            dicc[pais1][0] += 1
            dicc[pais2][2] += 1
        elif res2 > res1:
            dicc[pais2][0] += 1
            dicc[pais1][2] += 1
        else:
            dicc[pais1][1] += 1
            dicc[pais2][1] += 1
        
        rmix = leer_linea(mix)
    return dicc


def mostrar_listado(diccionario):

    lista = []

    for pais, datos in diccionario.items():

        if datos[0] > 0:
            lista.append((pais, datos[0]))
    
    lista.sort(key=lambda x: x[1], reverse=True)

    for pais in lista:

        print(f"{pais[0]} - {pais[1]}")

def main():

    # ejercicio 1
    america = open('america.csv', 'r')
    europa = open('europa.csv', 'r')
    mix = open('resultado.txt', 'w')

    merge(america, europa, mix)

    america.close()
    europa.close()
    mix.close()

    # ejercicio 2
    mix = open('resultado.txt', 'r')
    diccionario = generar_dicc(mix)
    mix.close()

    #ejercicio 3
    mostrar_listado(diccionario)

main()

