'''
Consigna:
    La salida del programa cuadrados.py es poco informativa. Modificar el pro-
    grama para que ponga el número junto a su cuadrado.

Pre-requisito:
    - Solo se deben ingresar número enteros postivos.
'''

def imprimir_cuadrados():

    n1 = int(input("Ingrese un número entero: "))
    n2 = int(input("Ingrese otro número entero: "))

    for x in range(n1, n2):
        print(f'el cuadrado de {x} es  { x * x}')

    print("Es todo por ahora")

imprimir_cuadrados()