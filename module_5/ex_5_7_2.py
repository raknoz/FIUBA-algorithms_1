'''
Consigna:
    Escribir una función que reciba un número entero k e imprima su descomposición en factores primos.
'''

def es_primo(n):
    '''
        Retorna true or false si un número es primo o no
    '''
    for d in range(n - 1, 1, -1):
        if n % d == 0:
            return False

    return True

def obtener_primos(k):
    '''
        Obtiene los números primos anterioes a K
    '''
    primos = []
    for p in range(1, k):
        if es_primo(p):
            primos.append(p)
    
    primos.reverse()
    return primos


def descomponer_en_primos(k):
    primos = obtener_primos(k)
    result = []
    num = k
    indice = 0

    while num > 0 and indice < len(primos):
        primo = primos[indice]
        if primo <= num:
            num -= primo
            result.append(primo)
        
        if primo > num:
            indice += 1
    
    print('El número {} se descompone en los primos: {}'.format(k, result))
        

descomponer_en_primos(22)