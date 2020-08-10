'''
Consigna:
    Escribir una función que calcule recursivamente cuántos elementos hay en una pila, suponiendo que la pila sólo tiene los métodos apilar y desapilar, 
    y no altere el contenido de la pila.
'''
from Pila import Pila

contador = 0

def contador_recursivo(pila):
    ''' Función que calcula recursivamente cuantos elemetos tiene una pila.'''
    global contador
    elemento = pila.desapilar()
    if not elemento:
        return elemento
    else:
        contador += 1
        pila.apilar(contador_recursivo(pila))    
    return elemento  
