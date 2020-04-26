'''
Consigna:
    Escribir dos funciones que resuelvan los siguientes problemas:
        a) Dado un número entero n, indicar si es par o no.
        b) Dado un número entero n, indicar si es primo o no.
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
        return f'{num} no es un número primo'
        
    #Hay una teoría que indica que se puede saber solo con recorrer hasta 1 + la raíz cuadrada de num
    limite =  int(num**0.5) + 1
    for x in range(2, limite):
        if(num % x == 0):
            return f'{num} no es un número primo'
        
    return f'{num} es un número primo'
