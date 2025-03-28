"""11. Sabiendo que el peso de un mol de agua es igual a 18 g, escriba una función que
reciba el valor en gramos de agua, y devuelva el valor en moles."""

MASA_MOLAR_AGUA = 18  # g/mol

def grs_agua_a_moles(grs):
    return grs / MASA_MOLAR_AGUA

print(grs_agua_a_moles(36))