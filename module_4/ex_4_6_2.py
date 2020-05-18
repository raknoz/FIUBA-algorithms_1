'''
Consigna:
    Escribir una implementación propia de la función abs, que devuelva el valor absoluto de cualquier valor que reciba.
'''

def my_abs(num):
    '''
        Función que obtiene el módulo de un número.
    '''
    if num < 0:
        return (-1 * num)
    return num