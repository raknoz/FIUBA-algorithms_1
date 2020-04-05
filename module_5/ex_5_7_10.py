'''
Consigna:
    Escribir una función que reciba un número natural e imprima todos los números primos que hay hasta ese número.
'''

def es_primo(n):
    if(n == 1):
        return True
    for x in range(n-1, 1, -1):
        if(n % x == 0):
            return False
    return True

def imprimir_numeros_primos(m):
    primos = []
    
    for x in range(1, m):
        if(es_primo(x)):
            primos.append(x)
    
    print('Los nmúeros primos que hay hasta el {}, son: {}'.format(m, primos))


imprimir_numeros_primos(13)