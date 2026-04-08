import re
'''
Consigna:
    Escribir una función, llamada wc, que dado un archivo de texto, lo procese e imprima 
    por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.
'''

def contador_caracteres(_str):
    '''
        Función que se encarga de remover los caracteres especiales de una cadena y devolver la longitud de esa cadena.
    '''
    return len(_str)

def contador_palabras_letras(_str, c_palabras, c_letras):
    '''
        Función que recibe una linea de texto y la parsea para devolver la cantidad de palabras y caracteres que tiene la línea.
    '''
    l_palabras = _str.split()

    #re.sub('\W+','', _str)
    for p in l_palabras:
        #Remuevo todos los caracteres especiales y dejo solo las letras
        aux = re.sub('\W+','', p)
        #if p != ''
        if aux:
            c_palabras += 1
            
        c_letras += contador_caracteres(p)
    
    return c_palabras, c_letras        

    
def wc(_file):
    '''
        Función que  dado un archivo de texto, lo procese e imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.
    '''
    c_lineas = 0
    c_palabras = 0
    c_letras = 0

    with open(_file, 'r') as f:
        for _line in f:
            c_palabras, c_letras = contador_palabras_letras(_line, c_palabras, c_letras)
            c_lineas += 1
    
    print(f'El archivo tiene {c_lineas} lineas | {c_palabras} palabras | {c_letras} caracteres')