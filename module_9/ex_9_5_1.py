'''
Consigna:
    Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
    en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.
'''

def tuplas_a_diccionario(l):
    '''
        Función que recibe una lista y la convierte en un diccionario.
        Si la clave existe lo agrega a la misma y sino crea uno nueva.
    '''
    _dict = {}
    for e in l:
        if e[0] in _dict:
            lista = _dict.get(e[0])
            lista.append(e[1])
            _dict[e[0]] = lista
        else:
            _dict[e[0]] = [e[1]]

    return _dict