"""3. Escribir una función que reciba un valor y calcule el factorial del mismo. Si no se
puede calcular el factorial del valor recibido, la función deberá devolver 0, de lo
contrario deberá devolver el valor calculado."""

def calcular_factorial(num):
    if num < 0 or type(num) != int:
        fact = 0
    else:
        fact = 1
        for i in range(1, num+1):
            fact = fact * i
    return fact

print(calcular_factorial(2))