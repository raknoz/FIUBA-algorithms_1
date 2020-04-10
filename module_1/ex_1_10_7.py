'''
Consigna:
    Implementar algoritmos que resuelvan los siguientes problemas:
        a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.
        b) Dado un número entero n, imprimir su tabla de multiplicar.

Pre-requisitos:
    Los numeros ingresados deben ser enteros.
'''

def hacer_cuentas(n1, n2):
    print(f'Los numero seleccionados son {n1} y {n2} ')
    print(f'Los resultados son: Suma = {n1 + n2} | Resta= {n1 - n2} | Multipliacion= {n1 * n2} | Division= {n1 / n2}')

def tabla_multiplicar(num):
    for k in range(1, 11):
        print(f'{num} X {k} = {num * k }')


n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número entero: "))
hacer_cuentas(n1, n2)
num = int(input("Ingrese un número entero: "))
tabla_multiplicar(num)