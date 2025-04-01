"""1. Escribir una función que reciba el número de un mes, y devuelva el nombre del
mes.
Por ejemplo, si la función recibe un "1", deberá devolver: "Enero"
En caso que el mes recibido no sea válido, deberá devolver "Mes Inválido".
No debe imprimir el nombre, sólo devolver la cadena correspondiente."""

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def nombre_mes_by_nro(nro):
    if nro <= 0 or nro > 12:
        mes = "mes invalido"
    else:
        mes = meses[nro-1]
    return mes

print(nombre_mes_by_nro(12))

