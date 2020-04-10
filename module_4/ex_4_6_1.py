'''
Consigna:
    Escribir dos funciones que resuelvan los siguientes problemas:
        a) Dado un número entero n, indicar si es par o no.
        b) Dado un número entero n, indicar si es primo o no.

Pre-requisitos:
    - Los números ingresados deben ser enteros no negativos.
'''

def es_par(num):
    '''
        Retorna mensaje si el número ingresado es par o no.
    '''
    if num % 2 == 0:
        print('{} es par.'.format(num))
    else:
        print('{} es impar.'.format(num))


def es_primo(num):
    '''
        Retorna mensaje si es número es primo o no.
    '''
    if num in (0, 1):
        return print(f'{num} no es un número primo')

    for x in range(num-1 , 1, -1):
        if(num % x == 0):
            return print(f'{num} no es un número primo')
        
    return print(f'{num} es un número primo')


es_par(2)
es_par(5)

es_primo(0)
es_primo(1)
es_primo(3)
es_primo(6)


