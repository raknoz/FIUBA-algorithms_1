'''
Consigna:
    La salida del programa cuadrados.py es poco informativa. Modificar el programa para que ponga el número junto a su cuadrado.
'''

def imprimir_cuadrados():
    '''
        metodo que calcula e imprime cuadrados. solicita por pantalla el ingreso de dos numeros enteros 
        y realiza el calculo del cuadrado en el rango excluyente [primero; segundo) de numeros enteros entre estos.
    '''
    n1 = int(input("Ingrese un número entero: "))
    n2 = int(input("Ingrese otro número entero: "))

    for x in range(n1, n2):
        print(f'el cuadrado de {x} es  { x * x}')

    print("Es todo por ahora")

imprimir_cuadrados()