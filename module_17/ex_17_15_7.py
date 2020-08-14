'''
Consigna:
    Escribir una función que calcule recursivamente cuántos elementos hay en una pila, suponiendo que la pila sólo tiene los métodos apilar y desapilar, 
    y no altere el contenido de la pila.
'''
from Pila import Pila

def _contador_recursivo(pila):
    ''' Función que calcula recursivamente cuantos elemetos tiene una pila.'''
    elemento = pila.desapilar()
    if not elemento:
        return 0
    
    contador = 1 + _contador_recursivo(pila)
    pila.apilar(elemento)
    return contador


def contador_recursivo(pila):
    return _contador_recursivo(pila)