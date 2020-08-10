'''
Consigna:
    Escribir una funcion recursiva que encuentre el mayor elemento de una lista.
'''

def _encontrar_mayor(lista, maximo):
    ''' Función recursiva que encuentra el mayo en una lista.'''
    if len(lista) == 0:
        return maximo
    else:
        elemento = lista.pop()
        if elemento > maximo:
            maximo = elemento
        return _encontrar_mayor(lista, maximo)


def encontrar_mayor(lista):
    print(_encontrar_mayor(lista, lista.pop()))