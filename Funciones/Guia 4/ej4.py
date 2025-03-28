"""4. Escribir una función que reciba a través de sus parámetros, la base y la altura de
un rectángulo y devuelva, el perímetro y la superficie, respetando este orden."""

def calcular_per_y_sup(base, altura):
    per = 2 * base + 2 * altura
    sup = base * altura
    return per, sup

perimetro, superficie = calcular_per_y_sup(10, 5)

print(f"El perimetro es {perimetro}")
print(f"La superficie es {superficie}")