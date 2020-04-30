'''
Consigna:
    Utilice el programa anterior para generar una tabla de conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.
'''

def calcular_relacion(grados):
    '''
        Función que hace la conversión de F° a C°.
    '''
    return (grados - 32) * (5/9)

def convertir_fahrenheit_celsius():
    '''
        Función que imprime el valor de F° en C° desde 0 a 130.
    '''
    for g in range(0, 130, 10):
        print(f'Los grados {g} en Fahrenheit son {round(calcular_relacion(g), 2)} en Celsius.')

convertir_fahrenheit_celsius()