from ex_11_10_2 import guardar
'''
Consigna: 
    a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido
    tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave
    y el segundo como diccionario.
    b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo,
    y guarde el contenido del diccionario en el archivo, con el formato clave, valor.
'''

def cargar_dicionario(_dict, _line):
    '''
        Proceso que hace un split de _line y pone los datos dentro del diccionario.
    '''
    data = _line.split(',')
    _dict[data[0]] = data[1]

def cargar_datos(_arch):
    '''
        Función que recibe un nombre de archivo, cuyo contenido tiene el formato clave, valor y devuelva un diccionario 
        con el primer campo como clave y el segundo como diccionario.
    '''
    _dict = {}
    with open(_arch, 'r') as _file:
        for _line in _file:
            cargar_dicionario(_dict, _line)
    return _dict

def guardar_datos(_dict, _arch):
    '''
        Función reciba un diccionario y un nombre de archivo, y guarde el contenido del diccionario en el archivo,
        con el formato clave, valor.
    '''
    with open(_arch, 'w') as _file:
        for k,v in _dict.items():
            guardar(_file, f'{k}, {v}')
    print('Proceso finalizado')