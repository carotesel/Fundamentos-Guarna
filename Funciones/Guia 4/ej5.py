"""Escribir una función que reciba como parámetro una temperatura en grados
Fahrenheit y devuelva el valor en Celsius. Tener en cuenta que: F = (C * 1,8) +
32."""

# F - 32 = C * 9/5
# (F - 32) * 5/9 = C

def convertirFarenheitACelsius(far:int)->int:
    celsius = (far - 32) * 5/9 
    return celsius

print(convertirFarenheitACelsius(40))