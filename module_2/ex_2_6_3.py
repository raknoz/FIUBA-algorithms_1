'''
Consigna:
    Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius
'''

def calculateRelation(grado):
    return (grado - 32) * (5/9)

def convertFahrenheitCelsius(grado):
    print('Los grados {} en Fahrenheit son {} en Celsius.'.format(grado, round(calculateRelation(grado), 2)))


grado = float(input('Ingrese los grados Fahrenheit a calcular: '))
convertFahrenheitCelsius(grado)