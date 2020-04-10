'''
Consigna:
    Dada una lista de números enteros y un entero k, escribir una función que:
    a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
    b) Devuelva una lista con aquellos que son múltiplos de k.
'''

def separa_elementos(l, k):
    '''
        Función que devuelve tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
    '''
    mayores = []
    menores = []
    iguales = []

    for x in l:
        if x > k:
            mayores.append(x)
        elif x == k:
            iguales.append(x)
        else:
            menores.append(x)

    return menores, mayores, iguales


def devuelve_multiplos(l,k):
    '''
        Función que devuelve una lista con aquellos que son múltiplos de k.
    '''
    return [x for x in l if x % k  == 0]

#print(separa_elementos([1, 3, 2, 5, 9, 0], 2))
print(devuelve_multiplos([1, 3, 2, 5, 9, 0], 2))