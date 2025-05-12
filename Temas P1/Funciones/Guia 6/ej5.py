"""5. Escribir un programa que solicite el ingreso de valores que representarán una
cantidad de azúcar (sacarosa), en gramos. El programa deberá informar a cuántos
átomos de Carbono, Hidrógeno y Oxígeno, equivale.
Se debe validar que el valor ingresado sea un número entero positivo, de lo
contrario se debe indicar que el valor ingresado no es válido y solicitar un nuevo
valor.
El ingreso de valores finaliza cuando la cantidad ingresada es igual a 0."""


MASA_MOLAR_SACAROSA = 342  # g/mol
NRO_AVOGADRO = 6.022 * 10 ** 23

def grs_agua_a_moles(grs):
    return grs / MASA_MOLAR_SACAROSA

def moles_a_moleculas(moles):
    return moles * NRO_AVOGADRO

def atomos_en_molec_sacarosa(molec):
    oxig = 11 * molec
    hidrog = 22 * molec
    carb = 12 * molec
    return oxig, hidrog, carb

def grs_sacarosa_a_atomos(grs):
    moles = grs_agua_a_moles(grs)
    moleculas = moles_a_moleculas(moles)
    oxigeno, hidrogeno, carbono = atomos_en_molec_sacarosa(moleculas)
    return oxigeno, hidrogeno, carbono

nro = 1

while nro != 0:
    nro = int(input("ingrese cantidad de gramos de sacarosa: "))

    if nro != 0:
        if nro.is_integer() and nro > 0:
            o2, hidrog, carb = grs_sacarosa_a_atomos(nro)
            print(f"Átomos de oxígeno: {o2}")
            print(f"Átomos de hidrógeno: {hidrog}")
            print(f"Átomos de carbono: {carb}")
        else: 
            print("numero ingresado incorrecto.")

