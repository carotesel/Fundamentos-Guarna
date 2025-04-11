"""3. Escribir una función que reciba un entero y retorne una lista con los valores de la
sucesión de Fibonacci desde la posición 0 y hasta la posición correspondiente al
parámetro recibido.
Recordemos que la sucesión comienza con los número 0 y 1; y a partir de estos, cada
término es la suma de los dos anteriores."""

def sucesion_fibonacci(posicion_final):
    fibonacci = []

    if posicion_final >= 0:
        fibonacci.append(0)
    if posicion_final >= 1:
        fibonacci.append(1)
    
    indice = 2

    while indice <= posicion_final:
        siguiente = fibonacci[indice - 1] + fibonacci[indice - 2]
        fibonacci.append(siguiente)
        indice+= 1
    
    return fibonacci

print(sucesion_fibonacci(5))
    

      
