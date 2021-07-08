'''
Consigna:
    Escribir una función que reciba una lista ordenada y un elemento. Si el elemento se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
    no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición. (No utilizar lista.sort().)
'''

def agregar_elemento(l, x):
    '''
        Inserta en una lista ordenada un elemento y devuelve su posicíon.
    '''
    index = 0
    result = []
    flag = False
    while index < len(l) and not flag:
        if l[index] < x:
            result.append(l[index])
            index += 1
        else:
            result.append(x)
            #Agrego lo que resta recorrer de la lista
            result.extend(l[index::])
            flag = True
        
    #Si es el último elemento de la lista
    if not flag:
        result.append(x)

    return result

def busquda_binaria(l, x):
    '''
        Realiza un búsqueda binaria sobre una lista ordenada y devuelve su posición.
    '''
    inicio = 0
    fin = len(l) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if l[medio] == x:
           return medio
       
        if x < l[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1
    
    return -1


def busca_elemento_en_lista(l, x):
    '''
        Función que se encarga de buscar un elemento en la lista y devolver su posición y si no está lo agrega donde corresponde y 
        devuelve la posición de donde fue insertado.
    '''
    if x in l:
        print(f'La posición del elemento {x} en la lista es: {busquda_binaria(l, x)}')
    else:
        l = agregar_elemento(l, x)
        print(f'La posición del elemento {x} en la lista es: {busquda_binaria(l, x)}')