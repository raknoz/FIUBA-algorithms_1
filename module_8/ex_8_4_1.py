'''
    Consigna:
    Escribir una función que reciba una lista desordenada y un elemento, que:
    a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la cantidad de coincidencias encontradas.
    b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
    c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado por parámetro y devuelva una lista con las posiciones.
'''
def buscar_coincidencias(l, x):
    '''
        Función que recibe una lista de elementos desordenados y busca 
        uno que se le pasa por parámetro y devuelve la cantidad de coincidencias
    '''
    cont = 0
    for e in l:
        if x == e:
            cont += 1
    print(f'La cantidad de coincidencias de {x} son {cont}')

def primera_coincidencia(l, x):
    '''
         Función que recibe una lista de elementos desordenados y busca la primera coincidencia del elemento en la lista y devuelva su posición.
    '''
    index = 0
    while index < len(l):
        e = l[index]
        if e == x:
            return index
        index += 1
    
    return -1

def busca_todas_coincidencias(l, x):
    '''
        Función que busca todos los elementos que coincidan con el pasado por parámetro y devuelva una lista con las posiciones.
    '''
    completo = False
    cont = []
    l_tmp = l
    while not completo:
        pos = primera_coincidencia(l_tmp, x)
        if pos != -1:
            cont.append(len(l) - len(l_tmp) + pos)
            if pos == len(l_tmp) - 1:
                completo = True
            else:
                l_tmp = l_tmp[pos + 1::]
        else:
            completo = True
           
    return cont 