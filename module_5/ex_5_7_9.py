'''
Consigna:
Escribir una función que reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.
    a) Implementarla utilizando un ciclo for , desde el primer número hasta el segundo.
    b) Implementarla utilizando un ciclo while , que multiplique el primer número hasta que sea mayor que el segundo.
    c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?
'''

def multiplos_for(m, n):
    '''
        Función  que reciba dos números como parámetros, y devuelve cuántos múltiplos del primero hay, que sean menores que el segundo.
    '''
    contador = 0

    for v in range(m+1, n):
        if v % m == 0:
            contador += 1
    
    print('Entre {} y {} hay {} multiplos de {}'.format(m, n, contador, m))

def multiplos_while(m, n):
    '''
        Función  que reciba dos números como parámetros, y devuelve cuántos múltiplos del primero hay, que sean menores que el segundo.
    '''
    contador = 0
    inicio = m + 1
    while inicio < n:
        if inicio % m == 0:
            contador += 1
        inicio += 1

    print('Entre {} y {} hay {} multiplos de {}'.format(m, n, contador, m))
    

multiplos_for(5, 23)
multiplos_while(5, 23)