'''
Consigna:
    Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor o no.
'''

def estan_ordenados(l):
    '''
        Función que valida si una lista está ordenada.
    '''
    ls = sorted(l)
    if (ls == l):
        return print('Están ordenados')
    
    return print('No están ordenados')