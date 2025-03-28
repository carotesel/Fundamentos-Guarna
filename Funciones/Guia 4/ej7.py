"""Escribir una función que reciba una cantidad de segundos, y devuelva el
equivalente en días, horas, minutos, segundos. Devolver los valores en el orden
indicado."""

CANT_SEG_EN_1_MIN = 60
CANT_MINS_EN_1_H = 60
CANT_HORAS_EN_1_DIA = 24

def convertir_segundos(seg):
    segundos = seg
    minutos = seg / CANT_SEG_EN_1_MIN
    horas = minutos / CANT_MINS_EN_1_H
    dias = horas / CANT_HORAS_EN_1_DIA

    return segundos, minutos, horas, dias

print(convertir_segundos(3600))
