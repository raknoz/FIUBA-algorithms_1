'''
Consigna:
    Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
    
Pre-requisitos:
    - n1 tiene que ser mayor o igual a n2
'''

def paresEntreValores(n1, n2):
    for n in range(n1, n2 + 1):
        if(n%2 == 0):
            print(n)
    

n1 = int(input('Ingrese el limite inferior: '))
n2 = int(input('Ingrese el limite superior: '))
paresEntreValores(n1, n2)
