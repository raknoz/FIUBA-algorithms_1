'''
Consigna:
    Escribir un programa que permita al usuario ingresar un conjunto de notas, pre-guntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.
'''

def calcula_promedio(notas):
    '''
        Obtiene el promedio de una lista de notas
    '''
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas) 

def pide_notas():
    '''
        Proceso que pide notas mientras el usuario desee
    '''
    notas = []
    rta = 'S'

    while('S' == rta):
        nota = int(input('Ingrese una nota: '))
        notas.append(nota)
        rta = input('Desea ingresar una nota S / N: ')
    
    print('El promedio es: {}'.format(calcula_promedio(notas)))