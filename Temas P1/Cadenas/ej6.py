"""6) Escribir una función que reciba por parámetro un texto todo en mayúsculas.
La función deberá devolver el texto pero respetando la regla que indica que luego de un
punto la primer letra debe ser mayúscula, y el resto minúsculas."""

def convertir_texto(cadena):
    minus = cadena.lower()
    frases = minus.split(". ")
    oracion_mdificada = []

    for frase in frases:
        fraseModif = frase.capitalize()
        oracion_mdificada.append(fraseModif)
    texto_final = ". ".join(oracion_mdificada)
    return texto_final

print(convertir_texto("CARO ES CRACK. TOMA YOGUR."))
