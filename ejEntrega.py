import doctest

# Constantes
DIAS_SEMANA = 5
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

def calcular_totales_por_sucursal(ventas): #Calcula el total de ventas por sucursal.
    """
    Calcula el total de ventas por sucursal.

    >>> calcular_totales_por_sucursal([[200, 700, 500, 400, 300], [100, 100, 200, 300, 400], [700, 800, 900, 1000, 1100]])
    [2100, 1100, 4500]
    """
    totales = []
    for sucursal in ventas:
        total_sucursal = sum(sucursal)
        totales.append(total_sucursal)
    return totales

def calcular_total_semanal(totales): #Calcula el total semanal de ventas.
    """
    Calcula el total semanal de ventas.

    >>> calcular_total_semanal([2100, 1100, 4500])
    7700
    """
    return sum(totales)

def encontrar_sucursal_con_menos_ventas(totales): #Devuelve el índice de la sucursal que vendió menos.
    """
    Devuelve el índice de la sucursal que vendió menos.

    >>> encontrar_sucursal_con_menos_ventas([2100, 1100, 4500])
    1
    """
    return totales.index(min(totales))

def calcular_totales_por_dia(ventas): #Calcula el total de ventas por día y lo guarda en una lista (cada dia es la posicion).
    """
    Calcula el total de ventas por día.

    >>> calcular_totales_por_dia([[200, 700, 500, 400, 300], [100, 100, 200, 300, 400], [700, 800, 900, 1000, 1100]])
    [1000, 1600, 1600, 1700, 1800]
    """
    ventas_dia = [0] * DIAS_SEMANA
    for i in range(DIAS_SEMANA):
        for sucursal in ventas:
            ventas_dia[i] += sucursal[i]
    return ventas_dia

def encontrar_dia_con_mas_ventas(ventas_dia): #Devuelve el índice del día con más ventas.
    """
    Devuelve el índice del día con más ventas.

    >>> encontrar_dia_con_mas_ventas([1000, 1600, 1600, 1700, 1800])
    4
    """
    return ventas_dia.index(max(ventas_dia))

def mostrar_resultados(total_final, sucursal_menos, total_sucursal_menos, dia_mas_vendido, total_dia_mas_vendido): #Muestra los resultados por pantalla.
    print(f"El total semanal de ventas fue de: ${total_final}")
    print(f"La sucursal que vendió menos fue la {sucursal_menos + 1} y su total fue de: ${total_sucursal_menos}")
    print(f"El día que más ventas hubo fue el {DIAS[dia_mas_vendido]} y el total fue de: ${total_dia_mas_vendido}")

def main():
    ventas = [
        [200, 700, 500, 400, 300],  # Sucursal 1
        [100, 100, 200, 300, 400],  # Sucursal 2
        [700, 800, 900, 1000, 1100]   # Sucursal 3
    ]
    
    totales = calcular_totales_por_sucursal(ventas)
    total_final = calcular_total_semanal(totales)
    sucursal_menos = encontrar_sucursal_con_menos_ventas(totales)
    ventas_dia = calcular_totales_por_dia(ventas)
    dia_mas_vendido = encontrar_dia_con_mas_ventas(ventas_dia)
    
    mostrar_resultados(
        total_final,
        sucursal_menos,
        totales[sucursal_menos],
        dia_mas_vendido,
        ventas_dia[dia_mas_vendido]
    )

doctest.testmod(verbose=True)
main()
