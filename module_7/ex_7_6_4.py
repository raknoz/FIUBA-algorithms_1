'''
Consigna:
    Vectores
    a) Escribir una función que reciba dos vectores y devuelva su producto escalar.
    b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales. 
    c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
    d) Escribir una función que reciba un vector y devuelva su norma.
'''

def producto_escalar(v1, v2):
    '''
        Función que calcula el producto escalar de dos vectores de igual cantidad de elementos.
    '''
    result = 0
    for i, v in enumerate(v1):
        result += v * v2[i]
    
    return result

def magnitud_vector(vec):
    '''
        Función que devuelve la magnitud de un vector, suma las potencias cuadradas de sus elementos y
        luego le calcula la raiz cuadrada 
    '''
    result = 0
    
    for v in vec:
        result += (v**2)
    
    #Potencia por 0.5 = raiz cuadrada
    return (result ** 0.5)

def calculo_producto_escalar(v1, v2):
    '''
        función que reciba dos vectores y devuelve su producto escalar.
    '''
    print(f'El producto escalar entre {v1} X {v2} es {producto_escalar(v1, v2)}')


def calculo_ortogonal(v1, v2):
    '''
        función que reciba dos vectores y devuelve si son o no ortogonales. 
    '''
    es_cero = 'No' if not producto_escalar(v1, v2) == 0 else 'Si'

    print(f'Los dos vectores {v1} y {v2} {es_cero} son ortogonales')


def vectores_paralelos(v1, v2):
    '''
        función que reciba dos vectores y devuelve si son paralelos o no.
    '''
    pd = producto_escalar(v1, v2)
    mag = round(magnitud_vector(v1) * magnitud_vector(v2), 2)
    #Si el coseno es 1 o -1 los vectores son paralelos.
    cos =  'son' if (pd / mag) in (-1, 1) else 'no son'
    
    print(f'Los dos vectores {v1} y {v2} {cos} paralelos')