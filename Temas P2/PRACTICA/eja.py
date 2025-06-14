"""### A)

El famoso torneo de tenis **Roland Garros** se disputa todos los años. 
Los resultados se guardan en el archivo `resultados.csv`. 
Este archivo tiene el siguiente formato:

día,participante1,puntos1_sets,participante2,puntos2_sets

El archivo se guarda en forma secuencial, 
comenzando desde el día 1 del campeonato, por lo que queda ordenado por día. 
Los partidos se juegan al mejor de cinco sets, 
en caso de ganar los tres primeros, no hace falta jugar los dos que le siguen, 
es por lo que hay partidos de tres, de cuatro y de cinco sets.

**Ejemplo:**

1,Jarry Nicolas,6-6-6,Dellien Hugo,4-4-2
1,Purcell Max,7-1-6-6,Thompson Jordan,5-6-4-4
2,Zapata Miralles,6-7-2-0-4,Schwartzman Diego,1-6-6-6-6
etc...


---

Se pide realizar un programa modular (compuesto por funciones), en Python que:

1. Recorriendo una sola vez el archivo de resultados y sin cargarlo 
completamente en memoria, haga un corte por día, indicando: 
día, cantidad de partidos jugados, cantidad de set jugados.
    
    Con nuestro ejemplo sería:
    
    ```
    Día       Partidos     Sets
    1         2            7
    2         1            5
    Etc.
    ```
    
2. Realizando una nueva lectura del archivo, arme un diccionario 
en donde la clave será el nombre del jugador y el dato la cantidad de partidos 
ganados. Tener en cuenta que gana el jugador que consigue tres sets.

3. En base al diccionario generado en el punto 2, dejar en el archivo 
`ganados.txt`, un listado, ordenado de mayor a menor por cantidad de 
partidos ganados, indicando por **cada línea del archivo**: 
el nombre del jugador – la cantidad de partidos ganados.

---

**IMPORTANTE:** Mantener las buenas prácticas recomendadas 
en el PEP de la cátedra: nombres, modularización, etc."""

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
    print("Dia - Partidos - Sets")


    while rarchivo != FIN_ARCHIVO:

        partidos = 0
        sets = 0
        dia_actual = rarchivo[0]

        while rarchivo[0] == dia_actual and rarchivo != FIN_ARCHIVO:
            
            partidos += 1
            lista_sets_jugador_1 = rarchivo[2].split('-')
            sets += len(lista_sets_jugador_1)
            
            rarchivo = leer_linea(archivo)

        print(f"{dia_actual} - {partidos} - {sets}")

def armar_diccionario(archivo):

        rarchivo = leer_linea(archivo)
        dicc = {}

        while rarchivo != FIN_ARCHIVO:

            jugador1 = rarchivo[1]
            resulatdos_jug_1 = rarchivo[2].split('-')
            sets_jug_1 = 0
            jugador2 = rarchivo[3]
            resulatdos_jug_2 = rarchivo[4].split('-')
            sets_jug_2 = 0

            for i in range(len(resulatdos_jug_1)):
                if int(resulatdos_jug_1[i]) > int (resulatdos_jug_2[i]):
                    sets_jug_1 += 1
                else:
                    sets_jug_2 += 1
            
            if sets_jug_1 > sets_jug_2:
                dicc.setdefault(jugador1, 0)
                dicc[jugador1] += 1
            else:
                dicc.setdefault(jugador2, 0)
                dicc[jugador2] += 1
            
            rarchivo = leer_linea(archivo)

        return dicc

def armar_listado(diccionario, resultante):
    lista = []

    for jugador, partidos in diccionario.items():
        lista.append((jugador, partidos))

    lista.sort(key=lambda x: x[1], reverse=True)

    for item in lista:
        linea = f"{item[0]} - {item[1]}\n"
        resultante.write(linea)

def main():

    # ej 1
    archivo = open('resultados.csv', 'r')
    corte_control(archivo)
    archivo.close()

    # ej 2
    archivo = open('resultados.csv', 'r')
    diccionario = armar_diccionario(archivo)
    archivo.close()

    # ej 3
    resultante = open('ganados.txt', 'w')
    armar_listado(diccionario, resultante)
    resultante.close()

main()

            




        
