'''
Consigna:
    Campaña electoral
    a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el mensaje Estimado <nombre>, vote por mí.
    b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una cantidad n , e imprima el mensaje anterior para los n nombres que se encuentran a partir
    de la posición p .
    c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario, para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.
'''

def imprimir_tupla_generica(nombres):
    '''
        Imprime el contenido de una tupla sin tener en cuenta el género
    '''
    for n in nombres:
        print(f'Estimado {n}, vote por mí.')

def imprimir_tupla(votantes):
    '''
        Imprime el contenido de una tupla teniendo en cuenta el género
    '''
    for n, g in votantes:
        saludo = 'Estimada' if  g == 'F' else 'Estimado'
        print(f'{saludo} {n}, vote por mí.')

def imprimir_tupla_posiscion(votantes, ini, total):
    '''
        Imprimer el mensaje para una cantidad total a partir de ini.
    '''
    fin = ini + total
    lista = votantes[ini:fin]
    imprimir_tupla_generica(lista)

def imprimir_tupla_genero(votantes, ini, total):
    '''
       Imprimer el mensaje para una cantidad total a partir de ini, distinguido por género.
    '''
    fin = ini + total
    lista = votantes[ini:fin]
    imprimir_tupla(lista)