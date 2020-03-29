'''
Consigna:
    Utilice el programa anterior para generar una tabla de conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.
'''

def calculateRelation(grado):
    return (grado - 32) * (5/9)

def convertFahrenheitCelsius():
    for g in range(0, 130, 10):
        print('Los grados {} en Fahrenheit son {} en Celsius.'.format(g, round(calculateRelation(g), 2)))

convertFahrenheitCelsius()