'''
Consigna:
    Dada una lista de números enteros, escribir una función que:
    a) Devuelva una lista con todos los que sean primos.
    b) Devuelva la sumatoria y el promedio de los valores.
    c) Devuelva una lista con el factorial de cada uno de esos números.
'''

def es_primo(n):
    '''
        Retorna True or False su un número es primo
    '''
    if n in (0, 1):
        return False
    
    for v in range (n - 1, 1, -1):
        if n % v == 0:
            return False
    
    return True

def calcula_factorial(n):
    '''
        Calcula el factorial de un número n
    '''
    if(n == 1):
        return 1
    
    return n * calcula_factorial(n-1)


def filtrar_primos(l):
    '''
        Función que retorna solo los números primos de una lista.
    '''
    l = [v for v in l if es_primo(v)]
    l.sort()
    print(f'Los números primos de la lista son: {l}')


def retorna_calculos(l):
    '''
        Función que devuelve la sumatoria y el promedio de los valores.
    '''
    return sum(l), sum(l)/len(l)


def calcula_factorial_lista(l):
    '''
        Función que devuelve una lista con el factorial de cada uno de esos números.
    '''
    lista_factorial = []

    for n in l:
        lista_factorial.append(calcula_factorial(n))
    
    return lista_factorial    