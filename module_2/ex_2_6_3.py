'''
Consigna:
    Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius
'''

def calcular_relacion(grados):
    '''
        Realiza el cálculo de conversión.
    '''
    return (grados - 32) * (5/9)

def convertir_fahrenheit_celsius(grados):
    '''
        Conveirte grados Fahrenheit a grados Celsius.
    '''
    print(f'Los grados {grados} en Fahrenheit son {round(calcular_relacion(grados), 2)} en Celsius.')


grados = float(input('Ingrese los grados Fahrenheit a calcular: '))
convertir_fahrenheit_celsius(grados)