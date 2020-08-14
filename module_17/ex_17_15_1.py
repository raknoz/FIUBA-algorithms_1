'''
Consigna:
    Escribir una función recursiva que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
'''

def contador_digitos(n):
    ''' Recibe un número positivo y calcula la cantidad de dígitos'''
    if n < 10:
        return 1
    else:
        return 1 + contador_digitos(n // 10)