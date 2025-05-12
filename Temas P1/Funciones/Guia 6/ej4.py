"""4. Escribir un programa que solicite el ingreso de dos números, y luego informe los
números primos que hay entre esos dos números.
Se debe validar que los números ingresados sean enteros y además que el primer
número sea menor o igual que el segundo."""

def es_primo(num):
    es_primo = True

    for n in range(2, num):
        if num % n == 0:
            es_primo = False
    
    if num < 2: 
        es_primo = False
    
    return es_primo


num1 = input("Ingrese un valor entero: ")
num2 = input("Ingrese otro valor entero: ")

print(f"Números primos entre {num1} y {num2}:")

if (num1.isdigit() and num2.isdigit() and int(num1) <= int(num2)):
    for i in range (int(num1), int(num2)+1):
        if es_primo(i):
            print(f"{i}")
else:
    print("Entrada inválida. Asegúrese de ingresar dos enteros y que el primero sea menor o igual al segundo.")
