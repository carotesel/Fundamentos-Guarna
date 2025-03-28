"""3. Solicitar el ingreso de un número y luego informar si el número
ingresado es un número primo."""

num = int(input("Ingrese un numero: "))

def es_primo(num):
    es_primo = True

    for n in range(2, num):
        if num % n == 0:
            es_primo = False
    
    if num < 2: 
        es_primo = False
    
    return es_primo

primo = es_primo(num)

if (primo): 
    print(f"El numero {num} es primo")

else :
    print(f"El numero {num} no es primo")

