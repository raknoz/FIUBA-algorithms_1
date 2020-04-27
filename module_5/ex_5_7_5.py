'''
Consgina:
    a) Implementar el algoritmo de Euclides para calcular el máximo común divisor de dos números n y m, dado por los siguientes pasos.
        1. Teniendo n y m, se obtiene r, el resto de la división entera de m/n.
        2. Si r es cero, n es el mcd de los valores iniciales.
        3. Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
    b) Hacer un seguimiento del algoritmo implementado para los siguientes pares de números: (15, 9); (9, 15); (10, 8); (12, 6).
'''

def division_entera(a, b):
    return a % b

def calcular_mcd(m, n):
    r = division_entera(m, n)
    while r != 0:
        m = n
        n = r
        #print('M: {}  N: {}'.format(m, n))
        r = division_entera(m, n)

    print('Resultado: ', n)

#Parte B
calcular_mcd(15, 9)
calcular_mcd(9, 15)
calcular_mcd(10, 8)
calcular_mcd(12, 6)
    