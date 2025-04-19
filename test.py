def procesar_lista(inventario):
    diccionario = {}

    entradas_tot = 0
    salidas_tot = 0

    for item in inventario:
        accion = item[0]
        producto = item[1]
        cantidad = item[2]

        if accion == "entrada":
                entradas_tot += cantidad
        elif accion == "salida":
                salidas_tot += cantidad
            
        if producto not in diccionario:
                diccionario[producto] = [entradas_tot - salidas_tot, entradas_tot, salidas_tot]

        else:
                diccionario[producto][1] += entradas_tot
                diccionario[producto][2] += salidas_tot
    return diccionario

def listar_productos(diccionaario):
    lista = []
    for item, valores in diccionaario:
        lista.append([item, valores[0]])

    lista.sort(key = lambda x: x[1], reverse = True)
    print(lista)
        
