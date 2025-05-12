"""6. Escribir un programa que solicite el ingreso de una cantidad de átomos de
Carbono, una cantidad de átomos de Hidrógeno y una cantidad de átomos de
Oxígeno. Validar a medida que se ingresan las cantidades, que se trate de un
número entero y positivo, de lo contrario se deberá enviar el mensaje de “Valor
Inválido” y solicitar un nuevo valor.
Teniendo en cuenta que la composición del azúcar (sacarosa), es Carbono 12,
Hidrógeno 22 y Oxígeno 11; el programa deberá informar la cantidad de
moléculas de azúcar (sacarosa) a las que equivalen los valores ingresados, ó
indicar que las cantidades ingresadas no corresponden a moléculas de sacarosa."""

# Constantes de la composición de una molécula de sacarosa
CARBONO_POR_MOLECULA = 12
HIDROGENO_POR_MOLECULA = 22
OXIGENO_POR_MOLECULA = 11


def solicitar_entero_positivo(nombre_elemento):
    """Solicita al usuario un número entero positivo para un elemento químico."""
    valor = input(f"Ingresá la cantidad de átomos de {nombre_elemento}: ")
    while not valor.isdigit() or int(valor) <= 0:
        print("Valor inválido")
        valor = input(f"Ingresá la cantidad de átomos de {nombre_elemento}: ")
    return int(valor)


def calcular_moleculas_sacarosa(c, h, o):
    """Calcula la cantidad de moléculas de sacarosa posibles."""
    return min(c // CARBONO_POR_MOLECULA,
               h // HIDROGENO_POR_MOLECULA,
               o // OXIGENO_POR_MOLECULA)


def main():
    """Función principal del programa."""
    cantidad_carbono = solicitar_entero_positivo("Carbono")
    cantidad_hidrogeno = solicitar_entero_positivo("Hidrógeno")
    cantidad_oxigeno = solicitar_entero_positivo("Oxígeno")

    moleculas = calcular_moleculas_sacarosa(cantidad_carbono,
                                             cantidad_hidrogeno,
                                             cantidad_oxigeno)

    if moleculas >= 1:
        print("Se pueden formar", moleculas, "molécula(s) de sacarosa.")
    else:
        print("Las cantidades ingresadas no corresponden a moléculas de sacarosa.")


# Llamado al programa principal
main()
