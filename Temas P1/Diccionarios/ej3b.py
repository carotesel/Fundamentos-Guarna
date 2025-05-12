"""
3. Dado el diccionario "dic_materias" que tiene cargados los nombre de las materias
como clave, y como valor asociado, una lista con tres números enteros, que indican:
la cantidad de alumnos anotados (como primer valor), cantidad de alumnos que
rindieron el parcial (segundo valor), cantidad de alumnos que aprobaron el parcial
(tercer valor).
Se pide que escribas:
b) Una función que reciba el diccionario y que devuelva una lista de tuplas, formadas
por pares (materia, porcentaje_aprobados), ordenada de mayor a menor por
porcentaje de aprobados (en este caso, se calcula sobre la cantidad que rindieron)."""

#dic_materias = { "quimica": [cant_alumnos_anotados, cant_al_parcial, cant_al_aprobaron_parcial]}

# desercion = abandono de materia
def porcentaje_aprobados(materias):
    lista_materias = []

    for materia, cantidades in materias.items():
        porcentaje_aprobados = (cantidades[2] / cantidades[1]) * 100
        lista_materias.append((materia, porcentaje_aprobados))
    
    lista_materias.sort(key=lambda dupla: dupla[1], reverse=True)  # 👈 ORDENAR de mayor a menor
        
    return lista_materias

dic_materias = {
    "Matemática": [100, 40, 30],  # 40/100 rindieron → 40%
    "Física": [80, 50, 20],        # 50/80 rindieron → 62.5%
    "Química": [90, 45, 25],       # 45/90 rindieron → 50%
    "Historia": [70, 20, 10],      # 20/70 rindieron → 28.6%
    "Literatura": [50, 30, 25],    # 30/50 rindieron → 60%
}

print(porcentaje_aprobados(dic_materias))

    