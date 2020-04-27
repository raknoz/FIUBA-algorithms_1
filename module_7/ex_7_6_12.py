'''
    Consigna:
        Funciones que reciben funciones.
        a) Escribir una funcion llamada map, que reciba una función y una lista y devuelva la lista
        que resulta de aplicar la función recibida a cada uno de los elementos de la lista recibida.
        b) Escribir una función llamada filter, que reciba una función y una lista y devuelva una
        lista con los elementos de la lista recibida para los cuales la función recibida devuelve un
        valor verdadero.
        c) ¿En qué ejercicios de esta guía podría haber utilizado estas funciones?
'''

cuadrado = lambda x : x * x

def solo_pares(l):
    '''
        Función que devuelve sólo los números pares.
    '''
    return [x for x in l if x % 2 == 0]

def map(l, m):
    '''
        Función que recibe una lista y una función de mapeo y la aplica a toda la lista.
    '''
    result = []
    for e in l:
        result.append(m(e))
    return result

def filter(l, f):
    '''
        Función que recibe un filtro y una lista y devuelve la lista filtrada.
    '''
    return f(l)