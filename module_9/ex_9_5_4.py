'''
Consigna:
    Escribir una función que reciba un texto y para cada caracter presente en el texto
    devuelva la cadena más larga en la que se encuentra ese caracter.
'''

def procesa_palabra(palabra, _dict):
    '''
        Función que recorre cada palabra y valida si existe en el diccionario y en caso afirmativo se encarga 
        si la palabra actual es mayor a la palabra alamcenada (len) la reemplaza. Sino crea la nueva clave.
    '''
    for letra in palabra:
        if letra in _dict:
            if len(_dict.get(letra)) <= len(palabra):
                _dict[letra] = palabra
        else:
            _dict[letra] = palabra
    return _dict

def procesa_texto(t):
    '''
        función que recibe un texto y para cada caracter presente en el texto devuelva la cadena más larga en la que se encuentra ese caracter.
    '''
    palabras = t.split()
    _dict = {}

    for p in palabras:
        _dict = procesa_palabra(p, _dict)
    
    #Imprimo el diccionario
    print(_dict)

procesa_texto('hola mundo')

