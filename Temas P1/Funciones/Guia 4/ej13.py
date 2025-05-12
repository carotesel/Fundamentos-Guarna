"""Por cada molécula de agua, hay 2 átomos de hidrógeno y 1 de oxígeno.
Escribir una función que reciba la cantidad de moléculas de agua y devuelva; la
cantidad de átomos de hidrógeno y la cantidad de átomos de oxígeno, que
componen la cantidad de moléculas de agua recibida."""

def o2_e_hidrogeno_en_molec_agua(molec):
    oxig = 1 * molec
    hidrog = 2 * molec
    return oxig, hidrog

oxigeno, hidrogeno = o2_e_hidrogeno_en_molec_agua(3)
print(f"Átomos de oxígeno: {oxigeno}")
print(f"Átomos de hidrógeno: {hidrogeno}")