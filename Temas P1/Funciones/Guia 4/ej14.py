"""14. Ahora toma las funciones escritas en los ejercicios XX, y utilizalas en una
nueva función, que reciba la cantidad de gramos de agua, y retorne la cantidad
de átomos de hidrógeno y de átomos de oxígeno, que hay en la cantidad de
gramos de agua recibida."""

# GRS AGUA -> ATOMOS DE HIDROGENO, O2

MASA_MOLAR_AGUA = 18  # g/mol
NRO_AVOGADRO = 6.022 * 10 ** 23

def grs_agua_a_moles(grs):
    return grs / MASA_MOLAR_AGUA

def moles_a_moleculas(moles):
    return moles * NRO_AVOGADRO

def atomos_en_molec_agua(molec):
    oxig = 1 * molec
    hidrog = 2 * molec
    return oxig, hidrog

def grs_agua_a_atomos(grs):
    moles = grs_agua_a_moles(grs)
    moleculas = moles_a_moleculas(moles)
    oxigeno, hidrogeno = atomos_en_molec_agua(moleculas)
    return oxigeno, hidrogeno

o2, hidrog = grs_agua_a_atomos(50)
print(f"Átomos de oxígeno: {o2}")
print(f"Átomos de hidrógeno: {hidrog}")