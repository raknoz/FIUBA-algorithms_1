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
        #v % m == 0
        if not v % m:
            contador += 1
    
    print(f'Entre {m} y {n} hay {contador} multiplos de {m}')

def multiplos_while(m, n):
    '''
        Función  que reciba dos números como parámetros, y devuelve cuántos múltiplos del primero hay, que sean menores que el segundo.
    '''
    contador = 0
    inicio = m + 1
    while inicio < n:
        if not inicio % m:
            contador += 1
        inicio += 1

    print(f'Entre {m} y {n} hay {contador} multiplos de {m}')