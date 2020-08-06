''' 
Consigna:
    Escribir una funcion recursiva que reciba como parámetros dos cadenas a y b, y 
    devuelva una lista con las posiciones en donde se encuentra b dentro de a.
'''
import pprint

posiciones = []

def buscar_posicion(cadena, buscado, desde, largo):
    ''' Función wrapper.'''
    valor = cadena.find(buscado, desde)
    
    if valor == -1:
        return
    else:
        posiciones.append(valor)
        buscar_posicion(cadena, buscado, valor + largo, largo)


def posiciones_de(cadena, buscado):
    ''' Función que busca en una cadena si está presente un valor determinado.'''
    largo = len(buscado)
    desde = 0
    buscar_posicion(cadena,buscado, desde, largo)
    pprint.pprint(posiciones)