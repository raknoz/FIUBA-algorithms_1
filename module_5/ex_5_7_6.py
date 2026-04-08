'''
Consigna:
    a) Escribir una función es_potencia_de_dos que reciba como parámetro un número natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
    b) Escribir una función que, dados dos números naturales pasados como parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango formado por
    esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función
    es_potencia_de_dos , descripta en el punto anterior.
'''

def es_potencia_de_dos(n):
    '''
        función que recibe como parámetro un número natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
    '''
    result = 1

    if n == 1:
        return True

    # n % 2 != 0
    if n % 2:
        return False

    while(result < n):
        result *= 2
    
    if result == n:
        return True
    
    return False
    

def es_potencia_de_dos_rangos(n1, n2):
    '''
        función que dados dos números naturales pasados como parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango formado.
    '''
    result = [0]
    
    for n in range(n1, n2 + 1):
        if(es_potencia_de_dos(n)):
            result.append(n)

    return sum(result)