''' 
Consigna:
    Escribir una funcion recursiva que reciba como parámetros dos cadenas a y b, y 
    devuelva una lista con las posiciones en donde se encuentra b dentro de a.
'''

def _posiciones_de(texto, buscado, inicio, largo):
    valor = texto.find(buscado, inicio)
    if valor == -1:
        return []
    return [valor] + _posiciones_de(texto, buscado, valor + largo, largo)


def posiciones_de(a, b):
    return _posiciones_de(a,b, 0, len(b))