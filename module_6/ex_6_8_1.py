'''
Consigna:
    Escribir funciones que dada una cadena de caracteres:
    a) Imprima los dos primeros caracteres.
    b) Imprima los tres últimos caracteres.
    c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
    d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
    e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime 'reflejoojelfer' .
'''

def imprimir_caracteres_inicio(s):
    print(s[:2])

def imprimir_caracteres_fin(s):
    print(s[-3:])

def caracteres_salteados(s):
    '''
         Imprima dicha cadena cada dos caracteres
    '''
    print(s[::2])

def invertir_texto(s):
    print(s[::-1])

def adicionar_texto(s):
    print(s + s[::-1])

#imprimir_caracteres_inicio('hola')
#imprimir_caracteres_fin('chau')
#caracteres_salteados('recta')
#invertir_texto('hola mundo!')
#adicionar_texto('reflejo')