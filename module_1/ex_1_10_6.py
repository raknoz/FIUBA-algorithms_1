'''
Consigna: 
    Implementar un algoritmo que, dado un número entero n, permita calcular su factorial.
'''

def factorial(n):
    '''
        Función que calcula el factorial del número n, ingresado por parámetro.
    '''
    if n == 1:
        return 1
    
    return n * factorial(n-1)
    
value = int(input("Ingrese un número entero: "))
print(f'El factorial de {value} es {factorial(value)}')