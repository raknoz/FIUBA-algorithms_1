'''
Consigna:
    a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
    b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5. 
    Nota: utilizar la función split de las cadenas.
'''

def valida_fichas(t1, t2):
    '''
        Función que dada una tupla t1 verifica si sus elementos estan en t2.
    '''
    #Separo los elementos de una tupla para saber si alguno está en la otra
    a, b = t1
    if a in t2 or b in t2:
        return True
    return False

def fichas_encajan(t1, t2):
    '''
        Valida si dos tuplas t1 y t2, corresponden.
    '''
    if (valida_fichas(t1, t2)):
        print('Las fichas encajan')
    print('Las fichas no encajan')

def fichas_encajan_str(s):
    '''
        A partir de un string obtengo las fichas para compararlas
    '''
    fichas = s.split(' ')
    fichas_encajan(fichas[0].split('-'), fichas[1].split('-'))