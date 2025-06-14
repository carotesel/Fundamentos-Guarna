"""Ejercicio 4:
Se registran calificaciones en calificaciones.csv:
cuatrimestre,materia,apellido_nombre,nota

Ejemplo:
1,Física,Martinez Rosa,6
1,Historia,Gomez Ana,7
1,Matemática,Lopez Ana,9
1,Matemática,Perez Juan,8
1,Química,Ramirez Jorge,5
2,Biología,Torres Pablo,6
2,Física,González Pedro,5
2,Historia,Gomez Ana,8
2,Química,Perez Juan,7

...
Se pide:

Corte de control por cuatrimestre indicando: cantidad de exámenes por cuatrimestre 
y dentro de cada cuatrimestre, cantidad de aprobados (≥6) y reprobados.

Diccionario con clave=estudiante y valor=[materias_cursadas, promedio_general].

Lista de estudiantes ordenada de mayor a menor promedio, mostrando: 
estudiante - promedio. Solo incluir estudiantes con promedio ≥7.

ESTRUCTURA 

- LEER LINEA ✔
- CORTE CONTROL ✔
- GENERAR DICCIONARIO ✔
- GENERAR LISTA ORDENADA ✔
- MOSTRAR LISTA ✔
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

    archivo.readline() #saltea primera linea

    rarchivo = leer_linea(archivo)

    while rarchivo != FIN_ARCHIVO:
        cuatrimestre = rarchivo[0]
        cant_examenes = 0
        aprobados = 0
        reprobados = 0

        print(f"\nCuatrimestre actual: {cuatrimestre}")

        while rarchivo != FIN_ARCHIVO and rarchivo[0] == cuatrimestre:
            cant_examenes += 1
            if int(rarchivo[3]) >= 6:
                aprobados += 1
            else:
                reprobados += 1
            
            rarchivo = leer_linea(archivo)
        
        print(f"Examenes: {cant_examenes}")
        print(f"Aprobados: {aprobados}")
        print(f"Reprobados: {reprobados}")
        

def generar_diccionario(archivo):

    dicc = {}

    archivo.readline() #saltea primera linea

    rarchivo = leer_linea(archivo)

    while rarchivo != FIN_ARCHIVO:
        estudiante = rarchivo[2]
        dicc.setdefault(estudiante, [0, 0.0, 0, ""])
        materia = rarchivo[1]
        nota = int(rarchivo[3])

        if dicc[estudiante][3] == "" or materia not in dicc[estudiante][3].split(','):
            dicc[estudiante][0] += 1
            dicc[estudiante][2] += nota

            if dicc[estudiante][3] == "":
                dicc[estudiante][3] = materia
            else:
                dicc[estudiante][3] += ',' + materia
        
        dicc[estudiante][1] = dicc[estudiante][2] / dicc[estudiante][0]

        rarchivo = leer_linea(archivo)

    # Calcular promedio y limpiar diccionario
    for alumno in dicc:
        materias = dicc[alumno][0]
        suma = dicc[alumno][2]
        promedio = suma / materias if materias > 0 else 0
        dicc[alumno] = [materias, promedio]

    return dicc

def ordenar_diccionario(diccionario):
    lista_ordenada = []

    for alumno, datos in diccionario.items():

        promedio = datos[1]

        if promedio >= 7:
            lista_ordenada.append((alumno, promedio))
    
    lista_ordenada.sort(key=lambda x: x[1], reverse=True)
    return lista_ordenada

def mostrar_datos(lista):
    print(f"\nDatos obtenidos del diccionario:")
    for alumno in lista:
        print(f"{alumno[0]}: promedio de: {alumno[1]}")


def main():

    archivo = open('calificaciones.csv', 'r')
    corte_control(archivo)
    archivo.close()

    archivo = open('calificaciones.csv', 'r')
    diccionario = generar_diccionario(archivo)
    lista = ordenar_diccionario(diccionario)
    mostrar_datos(lista)
    archivo.close()
    

main()