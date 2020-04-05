'''
Consigna:
    Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición
    de salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.
'''
def pedir_numero():
    return int(input('Ingrese un número natural (-1 para cortar): '))

def corte_centinela():
    num = pedir_numero()
    numeros = []

    while(num != -1):
        numeros.append(num)
        num = pedir_numero()

    print('Se ingrsaron: {} números. La suma es: {} y el promedio es igual a: {}'.format(len(numeros), sum(numeros), sum(numeros) / len(numeros)))


corte_centinela()

