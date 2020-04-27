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

    while num != -1:
        numeros.append(num)
        num = pedir_numero()

    promedio = sum(numeros) / len(numeros) if len(numeros) else 0
    print(f'Se ingrsaron: {len(numeros)} números. La suma es: {sum(numeros)} y el promedio es igual a: {promedio}')

corte_centinela()