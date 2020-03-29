'''
Consigna: 
    Implementar un algoritmo que, dado un número entero n, permita calcular su factorial.

Pre-condicion: 
    - Se sebe ingresar un numero entero positivo.
'''

def factorial(n):
    
    if(n == 1):
        return 1
    else:
        return n * factorial(n-1)
    
value = int(input("Ingrese un número entero: "))
print('El factorial de {} es {}'.format(value, factorial(value)))