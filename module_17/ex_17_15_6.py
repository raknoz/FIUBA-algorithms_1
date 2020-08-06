'''
Consigna:
    Escribir una función recursiva que calcule recursivamente el n-ésimo número triangular.
'''

def numero_triangular(n):
    ''' Función que calcula el n-ésimo número triangular. '''
    if n == 0:
        return 0
    else:
        return n + numero_triangular(n - 1)