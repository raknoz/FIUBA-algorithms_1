import time

'''
Consigna:
    Manejo de contraseñas
        a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
        b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
        c) Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, utilizando la función sleep del módulo time .
        d) Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano ( True o False ).
'''

PASSWORD_VALID = 'H0l4_Mund0'
INTENTOS_VALIDOS = 3
SLEEP_INTENTOS = 5

def pedir_pass():
    return input('Ingrese una password para acceder: ')

def es_pass_valido(psw):
    return PASSWORD_VALID == psw

def pedir_pass_iterativo():
    '''
        programa que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
    '''
    psw = pedir_pass()

    while es_pass_valido(psw):
        print('Pasword incorrecta!')
        psw = pedir_pass()
    
    print('Binvenido usuario!')

def pedir_pass_limitado():
    '''
          programa que le pregunte al usuario la contraseña con la cantidad de intentos limitados
    '''
    psw = pedir_pass()
    intentos = 1

    while es_pass_valido(psw) and intentos < INTENTOS_VALIDOS:
        intentos +=1
        print('Pasword incorrecta!')
        psw = pedir_pass()

    if es_pass_valido(psw) and intentos <= INTENTOS_VALIDOS:
        print('Binvenido usuario!')
    else:
        print('Cantidad de intentos agotados!')

def pedir_pass_limitado_sleep():
    '''
          programa que le pregunte al usuario la contraseña con la cantidad de intentos limitados
          pero después de cada intento agregue una pausa cada vez mayor
    '''
    psw = pedir_pass()
    intentos = 1
    espera = SLEEP_INTENTOS

    while es_pass_valido(psw) and intentos < INTENTOS_VALIDOS:
        intentos +=1
        print('Pasword incorrecta! debe esperar {} segundos para volver a intentar'.format(espera))
        time.sleep(espera)
        espera += 5
        psw = pedir_pass()

    if es_pass_valido(psw) and intentos <= INTENTOS_VALIDOS:
        print('Binvenido usuario!')
    else:
        print('Cantidad de intentos agotados!')


#pedir_pass_iterativo()
#pedir_pass_limitado()
pedir_pass_limitado_sleep()