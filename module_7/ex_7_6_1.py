'''
Consigna:
    Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor o no.
'''

def estan_ordenados(l):
    ls = sorted(l)
    if (ls == l):
        return print('Están ordenados')
    
    return print('No están ordenados')

estan_ordenados([1, 2, 4, 6])
