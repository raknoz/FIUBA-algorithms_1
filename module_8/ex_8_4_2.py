'''
    Consigna:
        Escribir una función que reciba una lista de números no ordenada, que:
        a) Devuelva el valor máximo.
        b) Devuelva una tupla que incluya el valor máximo y su posición.
        c) ¿Qué sucede si los elementos son cadenas de caracteres? --> Compara por el ascii (ord)
        Nota: no utilizar lista.sort()
'''

def retorna_maximo(l):
    '''
        Retona el máximo de una lista
    '''
    l_max = None
    if len(l) > 1:
        l_max = l[0]
    else:
        return l[0]

    for n in l:
        if n > l_max:
            l_max = n
    
    return l_max

def retorna_maximo_tupla(l):
    '''
        Retona el máximo de una lista
    '''
    l_max = None
    if len(l) > 1:
        l_max = (0, l[0])
    else:
        return (0, l[0])

    for i, n in enumerate(l):
        if n > l_max[1]:
            l_max = (i, n)
    
    return l_max