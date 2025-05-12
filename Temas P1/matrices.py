"""
Dadas dos matrices cuadradas, realizar la suma de las mismas y mostrar la matriz resultante
"""

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

m2 = [[7,8,9],
      [4,5,6],
      [1,2,3]]

resultado=[]

for fila in range(len(m1)):
    fila_resultado=[]
    for columna in range(len(m1[fila])):
        fila_resultado.append(m1[fila][columna] + m2[fila][columna])
    resultado.append(fila_resultado)

print('Matriz 1: ', m1)
print('Matriz 2: ', m2)
print('Matriz resultado de la suma: ', resultado)