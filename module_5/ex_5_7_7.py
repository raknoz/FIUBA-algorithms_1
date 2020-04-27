'''
Consigna:
    a) Escribir una función que devuelva la suma de todos los divisores de un número n, sin incluirlo.
    b) Usando la función anterior, escribir una función que imprima los primeros m números tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m números
    perfectos).
    c) Usando la primera función, escribir una función que imprima las primeras m parejas de números (a, b), tales que la suma de los divisores de a es igual a b y la suma de los
        divisores de b es igual a a (es decir las primeras m parejas de números amigos).
    d) Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecución.
'''

def obtener_divisores(n):
    result = []
    for x in range(1, n):
        if n % x == 0:
            result.append(x)
    return result

def suma_divisores(n):
    '''
        Función que devuelva la suma de todos los divisores de un número n, sin incluirlo.
    '''
    return sum(obtener_divisores(n))

def obtener_numeros_perfectos(m):
    '''
        Función que imprime los primeros m números tales que la suma de sus divisores sea igual a sí mismo.
    '''
    calculado = []
    valor = 1
    while len(calculado) < m:
        suma_div = suma_divisores(valor)
        if suma_div == valor:
            calculado.append(valor)
        valor +=1
    return calculado

def obtener_numeros_amigos(m):
    '''
        Función que imprime las primeras m parejas de números (a, b), tales que la suma de los divisores de a es igual a b y la suma de los
        divisores de b es igual a a
    '''
    result = []
    valor = 1

    while len(result) < m:
        a = suma_divisores(valor)
        b = suma_divisores(a)
        #print(f'n: {valor} | a: {a} | b: {b}')
        if b == valor and a != b:
            if not result.__contains__([b, a]) and not result.__contains__([a, b]):
                result.append([b, a])
        valor += 1

    return result