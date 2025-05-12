"""3. Dado el diccionario "dic_materias" que tiene cargados los nombre de las materias
como clave, y como valor asociado, una lista con tres números enteros, que indican:
la cantidad de alumnos anotados (como primer valor), cantidad de alumnos que
rindieron el parcial (segundo valor), cantidad de alumnos que aprobaron el parcial
(tercer valor).
Se pide que escribas:
a) Una función que reciba el diccionario y devuelva una lista con las materias cuyo
índice de deserción sea mayor al 50% (esto se calcula teniendo en cuenta la cantidad
de alumnos que rindieron el parcial sobre la cantidad de anotados).
"""

#dic_materias = { "quimica": [cant_alumnos_anotados, cant_al_parcial, cant_al_aprobaron_parcial]}

# desercion = abandono de materia
def materias_alta_desercion(materias):
    lista_desercion = []

    for materia, cantidades in materias.items():
        if cantidades[1] / cantidades[0] > 0.5:
            lista_desercion.append(materia)
    return lista_desercion

dic_materias = {
    "Matemática": [100, 40, 30],  # 40/100 rindieron → 40%
    "Física": [80, 50, 20],        # 50/80 rindieron → 62.5%
    "Química": [90, 45, 25],       # 45/90 rindieron → 50%
    "Historia": [70, 20, 10],      # 20/70 rindieron → 28.6%
    "Literatura": [50, 30, 25],    # 30/50 rindieron → 60%
}

print(materias_alta_desercion(dic_materias))
    
# NO OLVIDAR EL .ITEMS() PARA ACCEDER A LOS VALORES DE UN DICCIONARIO!