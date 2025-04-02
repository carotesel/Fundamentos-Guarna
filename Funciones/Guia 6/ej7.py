"""7. Escribir un programa que solicite el ingreso de un texto que será enviado
mediante un telegrama. Luego de ingresado, se deberá informar la cantidad de
palabras que lo componen y el importe a abonar por el solicitante.
El texto sólo puede contener, letras, números y los siguientes signos de
puntuación: . , ; : ()
Para el cálculo de las palabras, considerar que una palabra estará separada de
otra, por uno ó más blancos.
Para el cálculo del importe a abonar, deberá considerar que cada palabra pagará
$10 por cada 3 caracteres. Por las fracciones menores a los 3 caracteres, pagará
$8."""

PRECIO_3_CARACTERES = 10
PRECIO_FRACCIONES_MENORES_A_3 = 8
CARACTERES_PERMITIDOS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,;:()áéíóúÁÉÍÓÚñÑ"
text = input("Ingrese el texto a enviar por telegrama: ")

caracteres_no_permitidos = []
palabras = []
total = 0

for caracter in text:
    if caracter.lower() not in CARACTERES_PERMITIDOS.lower():
        caracteres_no_permitidos.append(caracter)

if caracteres_no_permitidos:
    print("Error. El texto contiene caracteres no permitidos.")
else:

    for palabra in text.split():
        if palabra:
            palabras.append(palabra)

    cantidad_palabras = len(palabras)

    # calcular costo

    for palabra in palabras:
        longitud = len(palabra)
        grupos_completos = longitud // 3
        grupos_fraccionarios = longitud % 3

        costoPalabra = grupos_completos * PRECIO_3_CARACTERES

        if grupos_fraccionarios > 0:
            costoPalabra += grupos_fraccionarios * PRECIO_FRACCIONES_MENORES_A_3
        
        total += costoPalabra
    
    # Mostrar resultados
    print("\nResumen del Telegrama:")
    print(f"Cantidad de palabras: {cantidad_palabras}")
    print(f"Importe a abonar: ${total}")

    
