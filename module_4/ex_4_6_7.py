'''
Consigna:
    Escribir un programa que reciba como entrada un entero representando un año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números
    romanos.
'''
NUMEROS_ROMANOS = {1000:'M', 900:'CM', 500:'D', 100:'C', 90:'XC', 50:'L', 10:'X', 9:'IX', 5:'V', 1:'I'}

def numeros_romanos(num):
    '''
        Función que retorna un número recibido en arábico a romano.
    '''
    n_romano = ''
    for valor in NUMEROS_ROMANOS.keys():
        result = num // valor
        if result > 0:
            for i in range(result):
                n_romano += NUMEROS_ROMANOS.get(valor)
            num = num % valor
    return n_romano