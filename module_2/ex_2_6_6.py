'''
Consigna:
    Escribir un programa que le pregunte al usuario un número n e imprima los primeros n números triangulares, junto con su índice. Los números triangulares se obtienen
    mediante la suma de los números naturales desde 1 hasta n.
'''

def calcularSuma(num):
    value = 0
    for n in range(1, num + 1):
        value+=n
    return value

def obtenerTriangulares(num):
    for n in range(1, num + 1):
        print('{} -> {}'.format(n, calcularSuma(n)))
    

num = int(input('Ingrese un número a calcular: '))
obtenerTriangulares(num)