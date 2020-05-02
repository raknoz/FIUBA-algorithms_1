import os
from ex_11_10_1 import abrir
'''
Condigna:
    Escribir una función, llamada cp, que copie todo el contenido de un archivo (sea de texto o binario) a otro, de modo que quede exactamente igual.
    Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.
'''
LIMIT_BYTES = 10

def generar_copia(_file, _mode):
    '''
        Función que recibe un path y el nombre de un archivo le genera el nombre de la copia
        en base al nombre original + "_copy"
    '''
    _path, _name = os.path.split(_file)
    _copy = os.path.join(_path, _name.replace('.','_copy.'))
    return abrir(_copy, _mode)

def cerrar(_file):
    '''
        Función que se encarga de cerrar un archivo.
    '''
    _file.close()

def guardar(_file, _data):
    '''
        Función que se encarga de guarlar la lista de bytes que se le pasan dentro de _file.
    '''
    _file.write(_data)

def cp(arch):
    '''
        Función que recibe un archivo y genera una copia complata del mismo.
    '''

    #Valido que exista ese archivo.
    if not os.path.isfile(arch):
        return print(f'{arch} no es un archivo!')
        
    with abrir(arch, 'rb') as f:
        #Genero el archivo nuevo
        cf = generar_copia(arch, 'bw')
        _bytes = f.read(LIMIT_BYTES)
        while _bytes:
            #Guardo los datos en el nuevo archivo
            guardar(cf, _bytes)
            #Vuelvo a leer los datos
            _bytes = f.read(LIMIT_BYTES)
        #Cierro el archivo copia
        cerrar(cf)
    
    return print(f'finalizó la copia de {arch}')