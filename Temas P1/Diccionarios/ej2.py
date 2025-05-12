"""2. Escribir una función que reciba por parámetro un texto, y devuelva un diccionario, el
cual tendrá como claves, cada una de las palabras que hay en el texto, y como valor,
la cantidad de ocurrencias de dicha palabra en el texto.
No distinguir entre mayúsculas y minúsculas.
Considerar que las palabras del texto estarán separadas por blancos. """

def cantidad_palabras(texto):

    dicc = {}

    texto = texto.lower()
    lista_palabras = texto.split() # devuelve una lista
    palabras_unicas = set(lista_palabras)

    for palabra in palabras_unicas:
        cant = texto.count(palabra)
        dicc[palabra] = cant
    
    print(dicc)

cantidad_palabras("hola soy hola soy soy caro y y y me gusta me amo")