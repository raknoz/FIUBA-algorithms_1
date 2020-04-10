'''
Consigna:
    Escribir una función que reciba un número natural e imprima todos los números primos que hay hasta ese número.
'''

def es_primo(n):
    '''
        Valida si un número es primo.
    '''
    if n in (0, 1):
        return False
    for x in range(n-1, 1, -1):
        if(n % x == 0):
            return False
    return True

def imprimir_numeros_primos(m):
    primos = []
    
    for x in range(1, m):
        if(es_primo(x)):
            primos.append(x)
    
    print(f'Los nmúeros primos que hay hasta el {m}, son: {primos}')


imprimir_numeros_primos(13)