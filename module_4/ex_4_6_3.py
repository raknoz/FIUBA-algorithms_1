'''
Consigna:
    Escribir una función que reciba por parámetro una dimensión n, e imprima la matriz identidad correspondiente a esa dimensión.
'''

def dibujar_matriz_identidad(n):
    '''
        Función que imprime la matriz identidad
    '''
    for f in range(1, n + 1):
        for c in range (1 , n + 1):
            valor = 0
            if c == f:
                valor = 1
            print(valor, end=' ')
        #Salto de linea
        print()