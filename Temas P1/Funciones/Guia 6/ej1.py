"""1. Escribir un programa que solicite el ingreso de 2 valores enteros y luego informe
el resultado de multiplicarlos, pero mediante sumas sucesivas.
Optimizar el cálculo, realizando la menor cantidad de ciclos posibles.
Tener en cuenta que el usuario puede ingresar valores negativos.
Para la solución NO utilices la función abs()."""

num1 = int(input("Ingrese un valor entero: "))
num2 = int(input("Ingrese otro valor entero: "))

tot = 0

if (num1 == 0 or num2 == 0):
    tot = 0
elif (num1 == num2):
    for i in range (1, num1+1):
        tot += num2
elif(num1 > num2):
    for i in range(1, num2+1):
        tot += num1
elif(num1 < num2):
    for i in range (1, num1+1):
        tot += num2

print(f"{num1} * {num2} = {tot}")