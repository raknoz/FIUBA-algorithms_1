'''
Consigna:
    Escribir una función empaquetar para una lista, donde epaquetar significa indicar la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones).
    Por ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5,1), (1, 2), (3, 2)]
'''

def empaquetar(l):
    '''
        Función que recorre una lista e indica la repetición de valores consecutivos.
    '''
    index = 0
    result = []
    
    while index < len(l):
        valor = l[index]
        contador = 0
        for x in range (index, len(l)):
            if l[x] == valor:
                contador += 1
            else:
                break
        
        index += contador
        result.append((valor, contador))

    return result