'''
Consigna:
    Diccionarios usados para contar.
    a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. 
    Por ejemplo, si recibe ”Qué lindo día que hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
    b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de texto, y los devuelva en un diccionario.
    c) Escribir una 
    función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
    dados.
    Nota: utilizar el módulo random para obtener tiradas aleatorias.
'''
import random

def contador_apariciones(l):
    '''
        Función que recibe una lista y devuelve un diccionario con el contador de coincidencias.
    '''
    _dict = {}
    for e in l:
        if e in _dict:
            _dict[e] = _dict.get(e) + 1
        else:
            _dict[e] = 1
    
    return _dict

def genera_tirada_dados():
    '''
        Genera una lista de combinaciones de dos dados
    '''
    tiradas = []
    for x in range(1, 20):
        tiradas.append((random.randrange(1, 7), random.randrange(1, 7)))

    return tiradas

def procesa_tirada_dados(l):
    '''
        Función que recibe una lista con tupas de tiradas de dados y las suma. 
        Devolviendo un mapa con las combinaciones
    '''
    print(f'Lista de tiradas: {l}')
    l_suma = []
    for d1, d2 in l:
        l_suma.append(d1 + d2)

    print(f'Lista con las sumas: {l_suma}')
    return contador_apariciones(l_suma)