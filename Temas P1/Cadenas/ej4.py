"""4) Escribir una función que reciba una palabra ó frase, y devuelva True, si es un palíndromo, ó False en caso
contrario. Asumir que la cadena a recibir, sólo estará formada por caracteres alfabéticos y espacios en
blanco.
Un palíndromo es una palabra o frase que es igual si se lee de izquierda a derecha que de derecha a
izquierda.
Ejemplos: Ana, ala, Neuquén, Oro, seres, radar
 Arriba la birra
 Amar da drama
 Luz azul
 La ruta natural """

def es_palindromo(cadena):
    cadena_sin_espacios = cadena.replace(" ", "")
    if str(cadena_sin_espacios).lower() == str(cadena_sin_espacios[::-1]).lower():
        palindromo = True
    else: 
        palindromo = False
    return palindromo

print(es_palindromo("Amar da drama"))