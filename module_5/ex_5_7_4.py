import random
'''
Consigna:
    Utilizando la función randrange del módulo random, escribir un programa que obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
    si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número correcto.
'''

def pedir_otro_numero(s):
    return  int(input(f'El número ingresado es {s}, ingrese otro nuevamente: '))

def pedir_numero():
    return int(input('Ingrese un número: '))

def generar_numero_random():
    return random.randint(0, 20)

def averigua_numero():
    acertijo = generar_numero_random()
    num = pedir_numero()

    while num != acertijo:
        if num > acertijo:
            num = pedir_otro_numero('mayor')
        else:
            num = pedir_otro_numero('menor')

    if num == acertijo:
        print('Acertó con el número!')