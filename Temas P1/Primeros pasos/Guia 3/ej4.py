"""Mostrar en forma descendente, los número pares entre 100 y 0
inclusive."""

for i in range (100, -1, -1):
    if i % 2 == 0:
        print(f"{i}")


