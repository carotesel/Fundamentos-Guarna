"""
1. Solicite el ingreso de una secuencia de valores, que termina con el valor 0.
A medida que solicita y se ingresa una valor se debe almacenar en una lista.
El valor 0 no debe almacenarse.
2. Muestre los valores ingresados.
3. Muestre los valores hasta encontrar el 3er. valor par ingresado inclusive.
En caso de haber ninguno o menos de 3 valores pares en la lista, se mostrarán
todos los valores.
4. Muestre los elementos que se encuentren en posiciones pares.
5. Muestre los elementos ordenados de mayor a menor, sin repetirlos."""

lista = []

def pedir_numeros():
    num = 1

    while num!= 0:
        num = int(input("Ingrese un numero: "))
        if num!= 0:
            lista.append(num)

def mostrar_numeros(lista):
    for n in lista:
        print(f"{n}")

def mostrar_pares(lista):
    pares_encontrados = 0
    resultado = []

    for num in lista:
        if pares_encontrados < 3:
            resultado.append(num)
            if num % 2 == 0:
                pares_encontrados += 1
    return resultado

def mostrar_pos_par(lista):
    i = 1
    while i < (len(lista)):
        if i % 2 == 0:
            print(f"{lista[i]}")
        i+=1

def ordenar_de_mayor_a_menor(lista):
    sin_repetidos = list(set(lista))  # elimina repetidos
    sin_repetidos.sort(reverse=True)    # ordena de mayor a menor (.sort el default es menor a mayor)
    return sin_repetidos


pedir_numeros()
print(ordenar_de_mayor_a_menor(lista))