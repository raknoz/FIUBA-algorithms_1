import random
'''
Consigna:
    Utilizando la función randrange del módulo random , escribir un programa que obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
    si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número correcto.
'''

def obtener_numero_random():
    return random.randint(0, 20)

def averigua_numero():
    acertijo = obtener_numero_random()
    print(acertijo)
    num = int(input('Ingrese un número: '))

    while num != acertijo:
        if(num > acertijo):
            num = int(input('El número ingresado es mayor, ingrese otro nuevamente: '))
        else:
            num = int(input('El número ingresado es menor, ingrese otro nuevamente: '))

    if num == acertijo:
        return print('Acertó con el número!')


averigua_numero()