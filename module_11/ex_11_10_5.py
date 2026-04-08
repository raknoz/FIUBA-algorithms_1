from ex_11_10_2 import generar_copia, abrir, guardar, cerrar
import os
'''
Consigna:
    Escribir una función, llamada rot13, que reciba un archivo de texto de origen y uno de destino, de modo que para 
    cada línea del archivo origen, se guarde una línea cifrada en el archivo destino. El algoritmo de cifrado a utilizar 
    será muy sencillo: a cada caracter comprendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo
    caracter.
'''
LETRAS = 'abcdefghijklmnopqrstuvwxyz'

def codificar(_chr):
    '''
        Función que codifica un caracter sumandole 13 a su posicíon y sacándole el módulo 26.
    '''
    pos = (LETRAS.index(_chr.lower()) + 13) % 26
    return LETRAS[pos] if _chr.islower() else LETRAS[pos].upper()

def codificar_linea(_line):
    '''
        Función que recorre una línea de teto y si es un caracter alfabético lo codifica y devuelve la línea 
        codificada.
    '''
    new_line = ''
    for c in _line:
        if c.isalpha():
            c = codificar(c)    
        new_line += c

    #Remuevo el último espacio
    return new_line

def rot13(_arch):
    '''
        Función que recorre un archivo y a cada línea le aplica una codificación y lo guarda en otro archivo
    '''
    with abrir(_arch, 'r') as _file:
        _copia = generar_copia(_arch, 'w')
        for _line in _file:
            code_line = codificar_linea(_line)
            guardar(_copia, code_line)
        cerrar(_copia)
    print('Finalizó la codificación')