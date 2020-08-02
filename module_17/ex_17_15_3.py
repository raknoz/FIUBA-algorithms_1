'''
Consigna: Escribir una función recursiva que reciba 2 enteros n y b y devuelva True si n es potencia de b.
'''

def rec_es_potencia(n, b, a):
    if n == b:
        return True
    if n < b:
        return False   
    else:
        return rec_es_potencia(n, b * a, a)


def es_potencia(n, b):
    return rec_es_potencia(n, b, b)