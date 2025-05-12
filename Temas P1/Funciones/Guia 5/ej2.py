"""2. Escribir una función que reciba un mes y un año; y devuelva la cantidad de días
del mes, considerando los años bisiestos.
Tenga en cuenta que un año bisiesto es aquel divisible por 4, salvo que sea
divisible por 100, en cuyo caso también debe ser divisible por 400."""

# voy a asumir que mes y año estan en formato numerico

cant_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0)

def cant_dias_mes(mes, anio):
    if mes <= 0 or mes > 12:
        print("mes invalido")
    else:
        if mes == 2 and es_bisiesto(anio):
            cantidad = 29
        else:
            cantidad = cant_dias[mes-1]
        
    return cantidad

print(cant_dias_mes(2, 2025))

                
