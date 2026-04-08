'''
Consigna: 
    Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima las líneas del archivo que contienen la cadena recibida.
'''

def contiene(_line, _str):
    '''
        Función que devuelve true o false si _str está incluida en la cadena _line.
    '''
    return _str.lower() in _line.lower()

def grep(_file, _str):
    '''
        Función que recibe una cadena y un archivo e imprima las líneas del archivo que contienen la cadena recibida.
    '''
    l_lineas = []

    with open(_file, 'r') as f:
        for _line in f:
            if contiene(_line, _str):
                l_lineas.append(_line)
        
    print(f'La cadena buscada: "{_str}" aparece en:')
    for linea in l_lineas:
        print(linea)